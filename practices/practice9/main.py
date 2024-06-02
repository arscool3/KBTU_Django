from dramatiq.results.errors import ResultMissing
from fastapi import FastAPI, HTTPException, Depends

from test import add_employee_task, result_backend

from datetime import datetime


from db import get_db

app = FastAPI()


def time_validation(iin: str):
    return iin

def check_time_minutes():
    current_time = datetime.now()
    minutes = current_time.minute
    if minutes % 2 == 0:
        return "Hello"
    else:
        raise HTTPException(status_code=400, detail="Try to say hello when minutes of time is even")


@app.get("/hello")
def get_user(response_based_on_time: str = Depends(check_time_minutes)):
    return response_based_on_time

def validate_iin_length(iin: str):
    if len(iin) < 8:
        raise HTTPException(status_code=400, detail="Error: IIN must be at least 8 characters long")
    else:
        return iin

@app.post("/add_employee")
def add_employee(iin: str = Depends(validate_iin_length), db = Depends(get_db)) -> dict:
    db.append(iin)
    task = add_employee_task.send(iin)
    return {'task_id': task.message_id}

@app.get("/get_employees")
def get_employees() -> list[str]:
    return get_db()



@app.get("/get_response")
def get_response(message_id: str):
    try:
        status = result_backend.get_result(add_employee_task.message().copy(message_id=message_id))
    except ResultMissing:
        return {"status": "pending"}
    return {'status': status}


def validate_new_data_length(data):
    if(len(data) < 8):
        raise HTTPException(status_code=400, detail="The length of new IIN is short")
    return data


@app.put("/update_employee/{iin}/{new_data}")
def update_employee(iin: str, new_data: str = Depends(validate_new_data_length), db = Depends(get_db)):
    index = db.index(iin)
    db[index] = new_data
    return db

@app.delete("/delete_employee/{iin}")
def delete_employee(iin: str):
    try:
        result = result_backend.get_result(add_employee_task.message().copy(iin=iin))
        if result == True:
            return {"message": "Employee deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail="Employee processing failed")
    except ResultMissing:
        raise HTTPException(status_code=404, detail="Employee processing task not found")
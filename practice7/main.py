from fastapi import FastAPI
from dramatiq.results.errors import ResultMissing

from task import credit_check_task, result_backend

app = FastAPI()


@app.post("/credit_check")
def credit_check(ssn: str) -> dict:
    task = credit_check_task.send(ssn)
    return {'task_id': task.message_id}


@app.get("/get_check")
def get_check(message_id: str):
    try:
        status = result_backend.get_result(credit_check_task.message().copy(message_id=message_id))
    except ResultMissing:
        return {"status": "pending"}
    return {'status': status}
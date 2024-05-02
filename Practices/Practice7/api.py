from fastapi import FastAPI
from dramatiq.results.errors import ResultMissing

from tasks import CheckStock_task, result_backend

app = FastAPI()


@app.post("/add_employee")
def CheckStock(artiqul: str) -> dict:
    task = CheckStock_task.send(artiqul)
    return {'task_id': task.message_id}


@app.get("/get_response")
def get_response(message_id: str):
    try:
        status = result_backend.get_result(CheckStock_task.message().copy(message_id=message_id))
    except ResultMissing:
        return {"status": "pending"}
    return {'status': status}


# redis
# task_queue 1 -> 2 -> 3
# backed_result: id: result, id_2: result

# pip install dramatiq redis fastapi uvicorn

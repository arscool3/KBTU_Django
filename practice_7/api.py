
from fastapi import FastAPI
from dramatiq.results.errors import ResultMissing

from tasks import add_order_task, result_backend

app = FastAPI()


@app.post("/add_order")
def add_order(order_id: str) -> dict:
    task = add_order_task.send(order_id)
    return {'task_id': task.message_id}


@app.get("/get_response")
def get_response(message_id: str):
    try:
        status = result_backend.get_result(add_order_task.message().copy(message_id=message_id))
    except ResultMissing:
        return {"status": "result is being looked for"}
    return {'status': status}


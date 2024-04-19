from fastapi import FastAPI

from dramatiq.results.errors import ResultMissing
from tasks import testing_task, result_back
app = FastAPI()


@app.post("/check_test")
def check_test_by_id(id: int) -> dict:
    task = testing_task.send(id)
    return {'task_id': task.message_id}


@app.get("check_result")
def check_result_by_message_id(message_id: int) -> dict:
    try:
        status = result_back.get_result(testing_task.message().copy(message_id=message_id))
    except ResultMissing:
        return {"status": "pending"}
    return {'status': status}

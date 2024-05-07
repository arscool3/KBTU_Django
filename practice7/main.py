from fastapi import FastAPI
from dramatiq.results.errors import ResultMissing

from tasks import check_license_and_category, result_backend

app = FastAPI()


@app.post("/evaluate_license")
def evaluate_license(iin: str) -> dict:
    task = check_license_and_category.send(iin)
    return {'task_id': task.message_id}


@app.get("/get_license_and_category")
def get_license_and_category(message_id: str):
    try:
        status = result_backend.get_result(check_license_and_category.message().copy(message_id=message_id))
    except ResultMissing:
        return {"status": "pending"}
    return {'status': status}
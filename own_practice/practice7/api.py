# api.py
from fastapi import FastAPI
from dramatiq.results.errors import ResultMissing

from tasks import evaluate_credit_task, result_backend

app = FastAPI()


@app.post("/evaluate_credit")
def evaluate_credit(ssn: str) -> dict:
    task = evaluate_credit_task.send(ssn)
    return {'task_id': task.message_id}


@app.get("/get_evaluation")
def get_evaluation(message_id: str):
    try:
        status = result_backend.get_result(evaluate_credit_task.message().copy(message_id=message_id))
    except ResultMissing:
        return {"status": "pending"}
    return {'status': status}

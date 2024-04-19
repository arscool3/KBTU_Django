from fastapi import FastAPI
from tasks import check_candidate_task

app = FastAPI()

@app.post("/check_candidate")
def check_candidate(candidate_id: int):
    task = check_candidate_task.send(candidate_id)
    return {'task_id': task.message_id}

@app.get("/get_task_status")
def get_task_status(task_id: str):
    result = check_candidate_task.get_result(task_id)
    if result is None:
        return {'status': 'pending'}
    else:
        return {'status': 'completed', 'result': result}
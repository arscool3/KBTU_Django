from fastapi import FastAPI
from dramatiq.results.errors import ResultMissing
from tasks import add_employee_task, result_backend

app = FastAPI()


@app.post("/ask_papers_score/{paper_id}") # GET academic papers (from midterm project) score from other service were they are scored by popularity 
def ask_papers_score(paper_id: str) -> dict:
    task = add_employee_task.send(paper_id, result_back)
    return {'task_id': task.message_id}


@app.get("/get_response")
def get_response(message_id: str):
    try:
        status = result_backend.get_result(ask_papers_score.message().copy(message_id=message_id))
    except ResultMissing:
        return "loading"
    return status
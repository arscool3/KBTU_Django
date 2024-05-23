from fastapi import FastAPI, BackgroundTasks
from dramatiq.results.errors import ResultMissing

from tasks import load_assignment_task, result_backend

app = FastAPI()
@app.post("/load_assignment/")
async def load_assignment(assignment_id: int):
    load_assignment_task.send()
    return {"message": "Assignment loading started"}

# FastAPI endpoint to retrieve the progress
@app.get("/progress/{message_id}")
async def get_progress(message_id: str):
    try:
        status = result_backend.get_result(load_assignment_task.message(message_id))
        if status == "Assignment loaded successfully":
            return {"status": "complete"}
        else:
            return {"status": "in_progress", "progress": status}
    except ResultMissing:
        return {"status": "pending"}
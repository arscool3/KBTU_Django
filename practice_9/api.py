from fastapi import FastAPI
from tasks import add_cosmetic_task, result_backend
from cosmetic import update_cosmetic, delete_cosmetic
from dramatiq.results.errors import ResultMissing
import random

app = FastAPI()

@app.post("/add_cosmetic")
def add_cosmetic(id: str) -> dict:
    task = add_cosmetic_task.send(id)
    return {'task_id': task.message_id}

@app.get("/get_response")
def get_response(message_id: str):
    try:
        status = result_backend.get_result(add_cosmetic_task.message().copy(message_id=message_id))
    except ResultMissing:
        return {"status": "pending"}
    return {'status': status}

@app.put("/update_cosmetic/{id}")
def update_cosmetic(id: str) -> dict:
    # Placeholder logic for updating a cosmetic item
    return {"message": f"Cosmetic item with ID {id} updated successfully"}

@app.delete("/delete_cosmetic/{id}")
def delete_cosmetic(id: str) -> dict:
    # Placeholder logic for deleting a cosmetic item
    return {"message": f"Cosmetic item with ID {id} deleted successfully"}


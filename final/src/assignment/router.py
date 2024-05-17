from fastapi import APIRouter
from assignment import schemas
from assignment import models
from assignment import crud
from typing import Annotated
from fastapi import Depends
from database import get_db
from assignment.task import *
from dramatiq.results.errors import ResultMissing

router = APIRouter(
    prefix='/assignment',
    tags=['assignment']
)

@router.post("/load_assignment")
async def load_assignment(assignment_id: int):
    load_assignment_task.send(assignment_id)
    return {"message": "Assignment loading started"}

# FastAPI endpoint to retrieve the progress
@router.get("/progress/{assignment_id}")
async def get_progress(assignment_id: str):
    try:
        status = result_backend.get_result(load_assignment_task.message(assignment_id))
        if status == "Assignment loaded successfully":
            return {"status": "complete"}
        else:
            return {"status": "in_progress", "progress": status}
    except ResultMissing:
        return {"status": "pending"}

@router.post("/")
def create_assignment(assignment: schemas.AssignmentCreate, session: Annotated[str, Depends(get_db)]):
    new_assignment = crud.create_assignment(assignment, session)

    return {"message": "assignment successfully added"}


@router.get("/{assignment_id}")
def get_assignment_by_id(assignment_id: int, session: Annotated[str, Depends(get_db)]):
    assignment = crud.get_assignment_by_id(assignment_id, session)

    return {"assignment": assignment}

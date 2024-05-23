from fastapi import APIRouter
from typing import Annotated
from fastapi import Depends
from database import get_db
from tasks.assignment_task import *
from dramatiq.results.errors import ResultMissing
from crud import assignment_crud as crud

from schemas.assignment_schemas import *
from utils.auth_utils import get_current_user

router = APIRouter(
    prefix='/assignment',
    tags=['assignment'],
    dependencies=[Depends(get_current_user)]
)

@router.post("/load_assignment")
async def load_assignment(assignment_id: int):
    load_assignment_task.send(assignment_id)
    return {"message": "Assignment loading started"}

@router.get("/progress")
async def get_progress(assignment_id: int):
    try:
        status = redis_client.get(assignment_id)
        if status == "Assignment loaded successfully":
            return {"status": "complete"}
        else:
            return {"status": "in_progress", "progress": status}
    except ResultMissing:
        return {"status": status}

@router.post("/")
def create_assignment(assignment: AssignmentCreate, session: Annotated[str, Depends(get_db)]):
    new_assignment = crud.create_assignment(assignment, session)

    return {"message": "assignment successfully added"}


@router.get("/{assignment_id}")
def get_assignment_by_id(assignment_id: int, session: Annotated[str, Depends(get_db)]):
    assignment = crud.get_assignment_by_id(assignment_id, session)

    return {"assignment": assignment}

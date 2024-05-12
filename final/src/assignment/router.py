from fastapi import APIRouter
from assignment import schemas
from assignment import models
from assignment import crud
from typing import Annotated
from fastapi import Depends
from database import get_db

router = APIRouter(
    prefix='/assignment',
    tags=['assignment']
)


@router.post("/")
def create_assignment(assignment: schemas.AssignmentCreate, session: Annotated[str, Depends(get_db)]):
    new_assignment = crud.create_assignment(assignment, session)

    return {"message": "assignment successfully added"}


@router.get("/{assignment_id}")
def get_assignment_by_id(assignment_id: int, session: Annotated[str, Depends(get_db)]):
    assignment = crud.get_assignment_by_id(assignment_id, session)

    return {"assignment": assignment}

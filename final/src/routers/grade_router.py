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
    prefix='/grades',
    tags=['grade'],
    dependencies=[Depends(get_current_user)]
)

@router.post("/")
def post_grade(grade: AssignmentCreate, session: Annotated[str, Depends(get_db)]):
    # new_assignment = crud.create_assignment(grade, session)

    return {"message": "assignment successfully added"}


@router.get("/{grade_id}")
def get_grade_by_id(grade_id: int, session: Annotated[str, Depends(get_db)]):
    assignment = crud.get_assignment_by_id(grade_id, session)

    return {"assignment": assignment}

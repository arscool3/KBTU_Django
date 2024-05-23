from fastapi import APIRouter, Depends
from database import get_db
from typing import Annotated
from utils.auth_utils import get_current_user 
from schemas import instructor_schemas as schemas
from crud import instructor_crud as crud

router = APIRouter(
    prefix='/instructor',
    tags=['instructor'],
    dependencies=[Depends(get_current_user)]
)

@router.get("/all")
def get_all_instructors(session: Annotated[str, Depends(get_db)]):
    instructors = crud.get_all_instructors(session)

    return {"instructor_list": instructors}

@router.get("/{instructor_id}")
def get_instructor_by_id(instructor_id: int, session: Annotated[str, Depends(get_db)]):
    instructor = crud.get_instructor_by_id(instructor_id, session)

    return {"instructor": instructor, "user": instructor.user}

@router.get("/{instructor_id}/courses")
def get_instructor_courses(instructor_id: int, session: Annotated[str, Depends(get_db)]):
    courses = crud.get_instructor_courses(instructor_id, session)

    return {"instructor_courses": courses}
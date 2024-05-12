from fastapi import APIRouter, Depends
from database import get_db
from student import crud
from typing import Annotated
from student import models

router = APIRouter(
    prefix='/student',
    tags=['student']
)


@router.get("/all")
def get_all_students(session: Annotated[str, Depends(get_db)]):
    students = crud.get_all_students(session)

    return {"student_list": students}

@router.get("/{student_id}")
def get_student_by_id(student_id: int, session: Annotated[str, Depends(get_db)]):
    student = crud.get_student_by_id(student_id, session)

    return {"instructor": student}
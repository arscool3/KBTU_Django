from typing import Annotated
from fastapi import Depends
from database import get_db
from models import student_models as models


def create_student(user_id: int, session: Annotated[str, Depends(get_db)]):
    new_student = models.Student(user_id=user_id)
    session.add(new_student)
    session.flush()

    return new_student

def get_all_students(session: Annotated[str, Depends(get_db)], skip: int = 0, limit: int = 100):
    return session.query(models.Student).offset(skip).limit(limit).all()

def get_student_by_id(student_id: int, session: Annotated[str, Depends(get_db)]):
    return session.query(models.Student).filter(models.Student.id==student_id).first()
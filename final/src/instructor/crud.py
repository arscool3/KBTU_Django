from instructor import schemas
from instructor import models
from typing import Annotated
from fastapi import Depends
from database import get_db
from sqlalchemy.orm import joinedload


def create_instructor(user_id: int, session: Annotated[str, Depends(get_db)]):
    new_instructor = models.Instructor(user_id=user_id)
    session.add(new_instructor)
    session.flush()

    return new_instructor


def get_all_instructors(session: Annotated[str, Depends(get_db)], skip: int = 0, limit: int = 100):
    return session.query(models.Instructor).options(joinedload(models.Instructor.user)).offset(skip).limit(limit).all()

def get_instructor_by_id(instructor_id: int, session: Annotated[str, Depends(get_db)]):
    return session.query(models.Instructor).filter(models.Instructor.id==instructor_id).first()

def get_instructor_courses(instructor_id: int, session: Annotated[str, Depends(get_db)], skip: int = 0, limit: int = 100):
    instructor = get_instructor_by_id(instructor_id, session)
    return instructor.courses
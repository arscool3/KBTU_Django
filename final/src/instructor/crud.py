from instructor import schemas
from instructor import models
from typing import Annotated
from fastapi import Depends
from database import get_db


def get_all_instructors(session: Annotated[str, Depends(get_db)], skip: int = 0, limit: int = 100):
    return session.query(models.Instructor).offset(skip).limit(limit).all()

def get_instructor_by_id(instructor_id: int, session: Annotated[str, Depends(get_db)]):
    return session.query(models.Instructor).filter(models.Instructor.id==instructor_id).first()

def get_instructor_courses(instructor_id: int, session: Annotated[str, Depends(get_db)], skip: int = 0, limit: int = 100):
    instructor = get_instructor_by_id(instructor_id, session)
    return instructor.courses
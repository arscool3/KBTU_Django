from typing import Annotated
from fastapi import Depends
from database import get_db
from models import course_models as models
from schemas import course_schemas as schemas

def create_course(course: schemas.CourseCreate, session: Annotated[str, Depends(get_db)]):
    new_course = models.Course(name=course.name, instructor_id=course.instructor_id)

    session.add(new_course)
    session.commit()
    session.refresh(new_course)

    return new_course


def get_course_by_id(course_id: int, session: Annotated[str, Depends(get_db)]):
    return session.query(models.Course).filter(models.Course.id==course_id).first()


def get_course_assignments(course_id: int, session: Annotated[str, Depends(get_db)]):
    course = get_course_by_id(course_id, session)

    return course.assignments



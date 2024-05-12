from fastapi import APIRouter
from course import schemas
from course import models
from typing import Annotated
from fastapi import Depends
from database import get_db

router = APIRouter(
    prefix='/course',
    tags=['course']
)


@router.post("/")
def create_course(course: schemas.CourseCreate, session: Annotated[str, Depends(get_db)]):
    new_course = models.Course(name=course.name, instructor_id=course.instructor_id)

    session.add(new_course)
    session.commit()

    return {"message": "course successfully added"}


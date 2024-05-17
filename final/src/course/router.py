from fastapi import APIRouter
from course import schemas
from course import models
from typing import Annotated, Any
from fastapi import Depends
from database import get_db
from auth.utils import require_scope
from auth.crud import get_user_by_id

router = APIRouter(
    prefix='/course',
    tags=['course']
)


@router.post("/")
def create_course(course: schemas.CourseCreate, session: Annotated[str, Depends(get_db)], scope: Annotated[Any, Depends(require_scope("instructor"))]):
    user = get_user_by_id(course.instructor_id)

    # new_course = models.Course(name=course.name, instructor_id=course.instructor_id)

    # session.add(new_course)
    # session.commit()

    return {"message": ""}





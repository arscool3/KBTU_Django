from fastapi import APIRouter
from typing import Annotated, Any
from fastapi import Depends
from database import get_db
from utils.auth_utils import require_scope, validate_user_by_email
from crud.instructor_crud import get_instructor_by_id
from crud.auth_crud import check_user_existense
from schemas import course_schemas as schemas

router = APIRouter(
    prefix='/course',
    tags=['course']
)


@router.post("/")
def create_course(course: schemas.CourseCreate, session: Annotated[str, Depends(get_db)], scope: Annotated[Any, Depends(require_scope("instructor"))]):
    user = get_instructor_by_id(course.instructor_id, session).user

    if validate_user_by_email(user.email, scope.email):
        create_course(course, session)
        return {"message": "course successfully created"}


@router.post("/add")
def add_course(course_id: int, session: Annotated[str, Depends(get_db)], scope: Annotated[Any, Depends(require_scope("student"))]):
    user = check_user_existense(scope.email, session)
    student = user.student
    student.courses.append( course_id)
    return {"mes": student}



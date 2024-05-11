from fastapi import APIRouter, Depends
from auth.utils import get_session
from typing import Annotated
from student import models

router = APIRouter(
    prefix='/student',
    tags=['student']
)


@router.get('/{student_id}/student_info')
def get_student_info(student_id: int, session: Annotated[str, Depends(get_session)]):
    student = session.query(models.Student).filter_by(id=1).first()
    return {"message": f"{student.courses}"}

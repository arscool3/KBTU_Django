from typing import Annotated
from fastapi import Depends
from database import get_db
from models import grade_models as models
from schemas import grade_schemas as schemas

def create_grade(grade: schemas.GradeCreate, session: Annotated[str, Depends(get_db)]):
    new_grade = models.Grade(assignment_id=grade.author_id, student_id=grade.student_id)

    session.add(new_grade)
    session.commit()
    session.refresh(new_grade)

    return new_grade


def get_grade_by_id(grade_id: int, session: Annotated[str, Depends(get_db)]):
    return session.query(models.Grade).filter(models.Grade.id==grade_id).first()



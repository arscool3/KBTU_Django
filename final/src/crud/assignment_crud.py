from database import get_db
from typing import Annotated
from fastapi import Depends
from schemas import assignment_schemas as schemas
from models import assignment_models as models

def create_assignment(assignment: schemas.AssignmentCreate, session: Annotated[str, Depends(get_db)]):
    new_assignment = models.Assignment(name=assignment.name, course_id=assignment.course_id)

    session.add(new_assignment)
    session.commit()
    session.refresh(new_assignment)

    return new_assignment

def get_assignment_by_id(assignment_id: int, session: Annotated[str, Depends(get_db)]):
    return session.query(models.Assignment).filter(models.Assignment.id==assignment_id).first()



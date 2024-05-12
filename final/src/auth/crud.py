from database import get_db
from auth import schemas
from auth import models
from typing import Annotated
from fastapi import Depends

def check_user_existense(email: str, session: Annotated[str, Depends(get_db)]):
   return session.query(models.User).filter(models.User.email==email).first()


# def get_assignment_by_id(assignment_id: int, session: Annotated[str, Depends(get_db)]):
#     return session.query(models.Assignment).filter(models.Assignment.id==assignment_id).first()



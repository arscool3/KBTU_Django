from database import get_db
from typing import Annotated
from fastapi import Depends
from exceptions.auth_exceptions import user_already_exists_exception
from utils.auth_utils import get_password_hash
from crud.instructor_crud import create_instructor
from crud.student_crud import create_student
from schemas import auth_schemas as schemas
from models import auth_models as models

def check_user_existense(email: str, session: Annotated[str, Depends(get_db)]):
   return session.query(models.User).filter(models.User.email==email).first()

def get_user_by_id(id: int, session: Annotated[str, Depends(get_db)]):
   return session.query(models.User).filter(models.User.id==id).first()


def create_user(user: schemas.UserCreate, session: Annotated[str, Depends(get_db)]): 
   if check_user_existense(user.email, session):
      raise user_already_exists_exception
   
   encrypted_password = get_password_hash(user.password)

   new_user = models.User(username=user.username, email=user.email, password=encrypted_password, role=user.role.value)

   session.add(new_user)
   session.flush()
   
   if(new_user.role == models.RoleEnum.INSTRUCTOR.value):  
      create_instructor(new_user.id, session)
        
   elif(new_user.role == models.RoleEnum.STUDENT.value):
      create_student(new_user.id, session)

   session.commit()

   return new_user



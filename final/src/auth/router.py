from fastapi import APIRouter
from auth import schemas
import models
import instructor.models as instructor_models
import student.models as student_models
from typing import Annotated
from fastapi import Depends, HTTPException
from auth.utils import *
from database import get_db

router = APIRouter(
    prefix='/auth',
    tags=['authentication']
)




@router.post('/register')
def register(user: schemas.UserCreate, session: Annotated[str, Depends(get_db)]):
    if check_user_existence(user, session):
        raise HTTPException(status_code=400, detail="Email already registered")

    encrypted_password = get_password_hash(user.password)

    new_user = models.User(username=user.username, email=user.email, password=encrypted_password, role=user.role.value)

    session.add(new_user)
    session.flush()
    if(new_user.role == models.RoleEnum.INSTRUCTOR.value):  
        new_instructor = instructor_models.Instructor(user_id=new_user.id)
        session.add(new_instructor)
        
    elif(new_user.role == models.RoleEnum.STUDENT.value):
        new_student = student_models.Student(user_id=new_user.id)
        session.add(new_student)

    session.commit()

    return {"message": "user successfully registered"}


@router.post('/login')
def login():
    pass
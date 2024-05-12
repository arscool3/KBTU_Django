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
    if not session.query(models.User).filter(models.User.email==user.email).first():
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
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], session: Annotated[str, Depends(get_db)]
) -> schemas.Token:
    user =authenticate_user(form_data.username, form_data.password, session)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={
            "sub": user.username,
            "role": user.role.value
            }, expires_delta=access_token_expires
    )
    return schemas.Token(access_token=access_token, token_type="bearer")
from fastapi import APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from auth import schemas
import models
from typing import Annotated
from fastapi import Depends, HTTPException,status
from auth.dependecies import *

router = APIRouter(
    prefix='/auth',
    tags=['authentication']
)


@router.post('/register')
def register(user: schemas.UserCreate, session: Annotated[str, Depends(get_session)]):
    if check_user_existence(user, session):
        raise HTTPException(status_code=400, detail="Email already registered")

    encrypted_password = get_password_hash(user.password)

    new_user = models.User(username=user.username, email=user.email, password=encrypted_password )

    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return {"message":"user created successfully"}


@router.post('/login')
def login():
    pass
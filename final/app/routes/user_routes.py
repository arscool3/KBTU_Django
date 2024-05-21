from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from crud.users import *
import schemas
import models
from db import get_db
from typing import Annotated

router = APIRouter()


@router.post("/register")
def register_user(user_create: schemas.UserCreate, db: Annotated[Session, Depends(get_db)]):
    db_user = get_user_by_email(db, email=user_create.email)
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    user = create_user(db, user_create)
    return {"message": "User created successfully"}

@router.post("/login")
def login_user(credentials: Annotated[OAuth2PasswordRequestForm, Depends()], db: Annotated[Session, Depends(get_db)]):
    username = credentials.username
    password = credentials.password
    user = authenticate_user(db, username, password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")
    access_token = create_access_token(user.id)
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/profile", response_model=schemas.User)
def get_user_profile(db: Annotated[Session, Depends(get_db)], token: str):
    current_user = get_current_user(db, token)
    return current_user


from passlib.context import CryptContext
from database import SessionLocal
from auth.schemas import UserCreate
from typing import Annotated, Union, Any
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends, HTTPException, status
from auth import models
from datetime import datetime, timedelta
from jose import jwt
from database import get_db
from auth import crud
from auth import schemas

SECRET_KEY = "01d31b6eb6cd66725a02f8c496a61fab4a08ed731e88d01d1e6180e046ef876b"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def authenticate_user(email: str, password: str, session: Annotated[str, Depends(get_db)]):
    user = crud.check_user_existense(email, session)
    if not user:
        return {"error": "user does not exist"}
    if not verify_password(password, user.password):
        return False
    return user



def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
from passlib.context import CryptContext
from database import SessionLocal
from auth.schemas import UserCreate
from typing import Annotated
from fastapi import Depends
import models

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

def check_user_existence(user: UserCreate, session: Annotated[str, Depends(get_session)]):
    existing_user = session.query(models.User).filter_by(email=user.email).first()
    return existing_user != None
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from passlib.context import CryptContext
import jwt
from datetime import datetime, timedelta

from models import User, Favorite
from schemas import UserCreate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = "secret"
ALGORITHM = "HS256"

def create_user(db: Session, user_create: UserCreate):
    hashed_password = pwd_context.hash(user_create.password)
    user = User(username=user_create.username, email=user_create.email, password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
    if user and pwd_context.verify(password, user.password):
        return user
    return None

def create_access_token(user_id: int):
    access_token_expires = timedelta(minutes=30)
    access_token_payload = {
        "sub": str(user_id),
        "exp": datetime.utcnow() + access_token_expires
    }
    access_token = jwt.encode(access_token_payload, SECRET_KEY, algorithm=ALGORITHM)
    return access_token

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_current_user(db: Session, token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token or missing user ID")
        return db.query(User).filter(User.id == user_id).first()
    except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Your token has expired. Please log in again.")


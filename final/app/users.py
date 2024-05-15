from datetime import timedelta, datetime
from typing import Optional
import jwt
from fastapi import APIRouter, Depends, BackgroundTasks, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from passlib.context import CryptContext
from pydantic import BaseModel
from sqlalchemy.orm import Session

import env
import models
import tasks
from db import SessionLocal

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}}
)

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
ALGORITHM = "HS256"
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="users/token")


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class User(BaseModel):
    username: str
    email: str
    password: str


@router.post("/register")
def create_user(user: User, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    user_model = models.User()

    user_model.username = user.username
    user_model.email = user.email
    user_model.password = user.password

    background_tasks.add_task(tasks.hash_password_and_save(user.username, user.password))

    db.add(user_model)
    db.commit()

    return {"message": "User registered successfully, password hashing in progress"}


def verify_password(plain_password: str, hashed_password: str):
    return bcrypt_context.verify(plain_password, hashed_password)


def authenticate(username: str, password: str, db=Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == username).first()

    if not user:
        return False

    hashed_password = tasks.redis_client.get(user.username)

    if not verify_password(password, hashed_password):
        return False

    return user


def create_access_token(username: str, user_id: int, expires_delta: Optional[timedelta] = None):
    encode = {"sub": username, "id": user_id}

    if expires_delta:
        expire = datetime.now() + expires_delta
        encode.update({"exp": expire})
    else:
        expire = datetime.now() + timedelta(minutes=15)
        encode.update({"exp": expire})

    token = jwt.encode(encode, env.SECRET_KEY, algorithm=ALGORITHM)

    return token


@router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db=Depends(get_db)):
    user = authenticate(form_data.username, form_data.password, db)

    if not user:
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )

    token_expires = timedelta(minutes=10)
    token = create_access_token(user.username, user.id, expires_delta=token_expires)

    return {"token": token, "token_type": "bearer"}


def get_current_user(token: str = Depends(oauth2_bearer)):
    try:
        payload = jwt.decode(token, env.SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        user_id: int = payload.get("id")
        if not username or not user_id:
            raise {"message": "user not found"}
        return {
            "username": username,
            "id": user_id
        }
    except Exception:
        raise HTTPException(status_code=400, detail="koroche kod ne rabochi")


@router.get("/me")
def me(current_user: User = Depends(get_current_user)):
    return current_user

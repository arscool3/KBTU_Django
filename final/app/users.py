from datetime import timedelta, datetime
from typing import Optional, Annotated
from jose import jwt, JWTError
from fastapi import APIRouter, Depends, BackgroundTasks, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from passlib.context import CryptContext
from pydantic import BaseModel
from sqlalchemy.orm import Session
import logging
import redis
from redis import Redis

import env
import models
from db import SessionLocal
import tasks

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}}
)

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
ALGORITHM = "HS256"
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="users/token")

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
redis_client = Redis(host="localhost", port=6379, db=0)


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


def verify_password(plain_password: str, hashed_password: str):
    return bcrypt_context.verify(plain_password, hashed_password)


def authenticate(username, password: str, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == username).first()

    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False

    return user


def create_access_token(username: str, user_id: int, expires_delta: Optional[timedelta] = None):
    encode = {"sub": username, "id": user_id}

    expire = datetime.utcnow() + expires_delta
    encode.update({"exp": expire})

    token = jwt.encode(encode, env.SECRET_KEY, algorithm=ALGORITHM)

    return token


def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    logger.debug(f"Token: {token}")
    try:
        payload = jwt.decode(token, env.SECRET_KEY, algorithms=[ALGORITHM])
        logger.debug(f"Payload decoded: {payload}")
        username: str = payload.get("sub")
        user_id: int = payload.get("id")
        if not username or not user_id:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return {
            "username": username,
            "id": user_id
        }
    except JWTError:
        raise HTTPException(status_code=400, detail="koroche kod ne rabochi")


@router.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    user = authenticate(form_data.username, form_data.password, db)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )

    token_expires = timedelta(minutes=10)
    token = create_access_token(user.username, user.id, token_expires)

    return {"token": token, "token_type": "bearer"}


@router.post("/register")
async def create_user(user: User,  db: Session = Depends(get_db)):
    user_model = models.User()

    user_model.username = user.username
    user_model.email = user.email
    user_model.password = user.password
    user_model.hashed_password = bcrypt_context.hash(user.password)

    db.add(user_model)
    db.commit()

    raise HTTPException(
        status_code=status.HTTP_201_CREATED,
        detail="User registered successfully"
    )


@router.post("/activate/{user_id}")
def activate_user(user_id, code: str, background_task: BackgroundTasks, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        return {"error": "User not found"}

    # return background_task.add_task(tasks.activate_user, user_id, code, db)

    value = redis_client.get(user.username)
    verification_code = value.decode("utf-8")
    logger.debug(f"value:{verification_code}{code}{user.username}")
    if verification_code == code:
        try:
            user.is_active = True
            db.add(user)
            db.commit()
            logger.info(f"User {user.username} activated successfully")
            return {"message": "User activated successfully"}
        except Exception as e:
            db.rollback()
            logger.error(f"Error activating user {user.username}: {str(e)}")
            return {"error": "Internal server error"}
    else:
        return {"error": "activation code not found"}


@router.get("/get_code")
def get_code(user_id, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        return {"error": "User not found"}

    code = tasks.get_activation_code(user.username)
    logger.debug(f"code:{code}")
    return {"code": code}


@router.get("/send_code")
def send_code(user_id, background_task: BackgroundTasks, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        return {"error": "User not found"}

    background_task.add_task(tasks.send_activate_number, user.username)
    return {'message': 'Code sended'}

@router.get("/me")
async def me(current_user: Annotated[dict, Depends(get_current_user)]):
    return current_user

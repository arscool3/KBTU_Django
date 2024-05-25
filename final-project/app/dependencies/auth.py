import base64
import json

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from passlib.context import CryptContext
from datetime import datetime, timedelta
from typing import Optional
from app.models.user import User
from app.dependencies.database import SessionLocal
import jwt

SECRET_KEY = "KBTUDjango"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

http_scheme = HTTPBearer()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def encode(data: dict):
    token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return token


def decode(token: str):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    data.update({"exp": expire})
    token = encode_token(data)
    return token


def encode_token(data: dict):
    header = {"alg": ALGORITHM, "typ": "JWT"}
    header_encoded = encode(header)
    data_encoded = encode(data)
    return header_encoded + b"." + data_encoded


def decode_token(credentials: HTTPAuthorizationCredentials):
    token = credentials.credentials
    data = token.split(".")
    payload = json.loads(base64.b64decode(data[4] + "===").decode("utf-8"))

    return payload


async def authenticate_user(username: str, password: str, db):
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


async def get_current_user(token: str = Depends(http_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = decode_token(token)
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except Exception:
        raise credentials_exception
    db = SessionLocal()
    user = db.query(User).filter(User.name == username).first()
    if user is None:
        raise credentials_exception
    return user

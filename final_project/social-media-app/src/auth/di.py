from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from datetime import datetime
from .models import User
from database import get_db
from .service import oauth2_bearer, SECRET_KEY, ALGORITHM


async def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_bearer)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        id: str = payload.get("id")
        expires: datetime = payload.get("exp")
        if datetime.fromtimestamp(expires) < datetime.now():
            return None
        if username is None or id is None:
            return None
        return db.query(User).filter(User.id == id).first()
    except JWTError:
        return None

# async def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_bearer)):
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username: str = payload.get("sub")
#         id: str = payload.get("id")
#         expires: datetime = payload.get("exp")
#         if datetime.fromtimestamp(expires) < datetime.now():
#             return None
#         if username is None or id is None:
#             return None
#         print(f"Decoded token: {payload}")  # Debugging line
#         user = db.query(User).filter(User.id == id).first()
#         print(f"User from DB: {user}")  # Debugging line
#         return user
#     except JWTError:
#         print("JWTError encountered")  # Debugging line
#         return None


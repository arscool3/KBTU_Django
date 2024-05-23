from fastapi import Depends, HTTPException
import jwt
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db
from app.models.user import User
from fastapi.security import OAuth2PasswordBearer
from app.core.config import settings
from app.auth.token import decode_access_token
import logging


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM

async def get_current_user(token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db)):
    try:
        payload = decode_access_token(token)
        # logger.info(f"JWT Payload: {payload}")
        user_id: int = int(payload.get("sub"))
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")
        user = await db.get(User, user_id)
        if user is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")
        return user
    except jwt.PyJWTError:  # Catch exceptions from pyjwt
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")

from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import datetime

from .schemas import UserCreate, UserUpdate, User as UserSchema
from ..database import get_db
from .service import (
    existing_user,
    create_access_token,
    get_current_user,
    create_user as create_user_svc,
    authenticate,
    update_user as update_user_svc,
)


router = APIRouter(prefix="/auth", tags=["auth"])


# signup
@router.post("/signup", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # check existing user
    db_user = await existing_user(db, user.username, user.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="username or email already in use",
        )

    db_user = await create_user_svc(db, user)
    access_token = await create_access_token(user.username, db_user.id)

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "username": user.username,
    }


# login to generate token
@router.post("/token", status_code=status.HTTP_201_CREATED)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    db_user = await authenticate(db, form_data.username, form_data.password)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="incorrect username or password",
        )

    access_token = await create_access_token(db_user.username, db_user.id)
    return {"access_token": access_token, "token_type": "bearer"}


# get current user
@router.get("/profile", status_code=status.HTTP_200_OK, response_model=UserSchema)
async def current_user(token: str, db: Session = Depends(get_db)):
    db_user = await get_current_user(db, token)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="token invalid"
        )

    return db_user


# update user
@router.put("/{username}", status_code=status.HTTP_204_NO_CONTENT)
async def update_user(
    username: str, token: str, user_update: UserUpdate, db: Session = Depends(get_db)
):
    db_user = await get_current_user(db, token)

    if db_user.username != username:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not authorized to update this user",
        )

    await update_user_svc(db, db_user, user_update)

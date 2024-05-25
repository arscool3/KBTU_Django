import json
from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.dependencies.auth import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token, verify_password, get_current_user
from app.models.user import User
from app.dependencies.database import SessionLocal, get_db
from app.schemas.user import UserCreate, UserBase

router = APIRouter()

@router.post("/login")
async def login_for_access_token(form_data: UserBase, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.name == form_data.username).first()
    if not db_user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": db_user.name}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me")
async def secure_endpoint(current_user: User = Depends(get_current_user)):

    return {"message": "This is a secure endpoint", "user": current_user}

@router.post("/register")
async def register(user: UserBase, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    db_user = User()
    db_user.name = user.username
    db_user.email = user.email
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
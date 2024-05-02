# routers/users.py
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import User
from schemas import UserCreate, UserDisplay

router = APIRouter()

@router.post("/users/", response_model=UserDisplay)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(username=user.username, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/users/", response_model=List[UserDisplay])
def read_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

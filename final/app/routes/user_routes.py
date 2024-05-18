from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from crud.user import *
from schemas import UserCreate, User
from db import get_db

router = APIRouter()

@router.post("/register")
def register_user(user_create: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user_create.email)
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    user = create_user(db, user_create)
    return {"message": "User created successfully"}

@router.post("/login")
def login_user(credentials: HTTPAuthorizationCredentials, db: Session = Depends(get_db)):
    username, password = credentials.credentials.split(":")
    user = authenticate_user(db, username, password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")
    access_token = create_access_token(user.id)
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/profile")
def get_user_profile(current_user: User = Depends(get_current_user)):
    return {"username": current_user.username, "email": current_user.email}


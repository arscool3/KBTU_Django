from datetime import timedelta
from auth.auth import authenticate_user, create_access_token, get_current_user, get_password_hash
from utils.utils import hash_pass
# from utils.utils import create_access_token
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import   OAuth2PasswordRequestForm

from sqlalchemy.orm import Session
from models.models import User as DBUser
from schemas.schemas import UserCreate, UserLogin
from database.database  import  get_db
from exceptions.exeptions import token_exception

user_router = APIRouter(prefix="/api", tags=["users"])

# Dependency to get database session


@user_router.post("/register")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    
    existing_user = db.query(DBUser).filter(DBUser.email == user.email).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hash_password = get_password_hash(user.password)
    new_user = DBUser(username = user.username,email = user.email, password = hash_password )
    new_user.is_active = True
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user

@user_router.post("/login")

async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(),
                                 db: Session = Depends(get_db)):

    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise token_exception()
    token_expires = timedelta(minutes=20)
    
    token = create_access_token(user, expires_delta=token_expires)
    return {"token": token}


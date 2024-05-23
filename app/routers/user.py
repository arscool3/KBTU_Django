from fastapi import APIRouter, HTTPException, Depends
import httpx
from sqlalchemy.ext.asyncio import AsyncSession
from passlib.context import CryptContext
from pydantic import BaseModel
from app.db.database import get_db
from app.models.user import User
import logging
from sqlalchemy.future import select
from typing import List 
from app.schemas.user import UserResponse

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

# Configure logging
# logging.basicConfig(level=logging.DEBUG)

@router.post("/register")
async def register(user: UserCreate, db: AsyncSession = Depends(get_db)):
    # Check if user already exists
    async with db.begin():
        result = await db.execute(select(User).filter(User.email == user.email))
        existing_user = result.scalars().first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = pwd_context.hash(user.password)
    db_user = User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    # logging.debug(f"User registered with ID: {db_user.id}")
    return db_user

@router.get("/{user_id}")
async def get_user_by_id(user_id: int, db: AsyncSession = Depends(get_db)):
    # Retrieve the user from the database by ID
    user = await db.get(User, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Return the user
    return user

@router.get("/", response_model=List[UserResponse])
async def get_all_users(db: AsyncSession = Depends(get_db)):
    # Retrieve all users from the database
    users = await db.execute(select(User))
    return users.scalars().all()


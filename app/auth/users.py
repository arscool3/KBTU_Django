from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user import UserCreate, UserOut
from app.models.user import User
from app.core.security import get_password_hash, verify_password
from app.db.session import get_session
from app.core.config import settings
from jose import JWTError, jwt

router = APIRouter()

async def create_user(user: UserCreate, session: AsyncSession):
    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=get_password_hash(user.password)
    )
    session.add(db_user)
    await session.commit()
    await session.refresh(db_user)
    return db_user

@router.post("/register", response_model=UserOut)
async def register_user(user: UserCreate, session: AsyncSession = Depends(get_session)):
    db_user = await session.get(User, user.username)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered"
        )
    return await create_user(user, session)

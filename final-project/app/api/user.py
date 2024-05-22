from fastapi import APIRouter, Depends, HTTPException
from app.models.book import Book
from app.models.user import User
from app.dependencies.auth import get_current_user

router = APIRouter()


@router.get("/users/me/")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
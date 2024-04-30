from fastapi import APIRouter, HTTPException
from database import db
from models import User, Post, Comment
from typing import List

user_router = APIRouter(prefix="/users")
post_router = APIRouter(prefix="/posts")
comment_router = APIRouter(prefix="/comments")

@user_router.get("/{user_id}", response_model=User)
async def get_user(user_id: int):
    for user in db.users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")


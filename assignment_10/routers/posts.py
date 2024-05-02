from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Post
from schemas import PostCreate, PostDisplay

router = APIRouter()

@router.post("/posts/", response_model=PostDisplay)
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    db_post = Post(title=post.title, content=post.content, user_id=post.user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

@router.get("/posts/", response_model=List[PostDisplay])
def read_posts(db: Session = Depends(get_db)):
    posts = db.query(Post).all()
    return posts

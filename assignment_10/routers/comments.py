from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Comment
from schemas import CommentCreate, CommentDisplay

router = APIRouter()

@router.post("/comments/", response_model=CommentDisplay)
def create_comment(comment: CommentCreate, db: Session = Depends(get_db)):
    db_comment = Comment(content=comment.content, user_id=comment.user_id, post_id=comment.post_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

@router.get("/comments/", response_model=List[CommentDisplay])
def read_comments(db: Session = Depends(get_db)):
    comments = db.query(Comment).all()
    return comments

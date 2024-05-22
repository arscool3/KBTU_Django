from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from db import get_db
import crud.comments as crud
from crud.users import get_current_user
import models
import schemas

router = APIRouter()

@router.post("/comments/", response_model=schemas.Comment)
def create_comment(token: str, comment: schemas.CommentCreate, db: Session = Depends(get_db)):
    current_user = get_current_user(db, token)
    return crud.create_comment(db=db, comment=comment, user_id = current_user.id)

@router.get("/comments/{comment_id}", response_model=schemas.Comment)
def get_comment(comment_id: int, db: Session = Depends(get_db)):
    db_comment = crud.get_comment(db=db, comment_id=comment_id)
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return db_comment

@router.get("/papers/{paper_id}/comments", response_model=List[schemas.Comment])
def get_paper_comments(paper_id: int, db: Session = Depends(get_db), skip: int = 0, limit: int = 10):
    return crud.get_paper_comments(db=db, paper_id=paper_id, skip=skip, limit=limit)

@router.put("/comments/{comment_id}", response_model=schemas.CommentCreate)
def update_comment(token: str, comment_id: int, comment: schemas.CommentCreate, db: Session = Depends(get_db)):
    current_user = get_current_user(db, token)
    db_comment = crud.update_comment(db=db, comment_id=comment_id, user_id = current_user.id ,comment=comment)
    return db_comment

@router.delete("/comments/{comment_id}")
def delete_comment(token: str, comment_id: int, db: Session = Depends(get_db)):
    current_user = get_current_user(db, token)
    crud.delete_comment(db=db, comment_id=comment_id, user_id = current_user.id)


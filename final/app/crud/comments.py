from sqlalchemy.orm import Session
from fastapi import HTTPException, status
import models
import schemas

def create_comment(db: Session, comment: schemas.CommentCreate, user_id: int):
    db_comment = models.Comment(**comment.dict(), author_id=user_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

def get_comment(db: Session, comment_id: int):
    return db.query(models.Comment).filter(models.Comment.id == comment_id).first()

def get_paper_comments(db: Session, paper_id: int, skip: int = 0, limit: int = 10):
    return db.query(models.Comment).filter(models.Comment.paper_id == paper_id).offset(skip).limit(limit).all()


def update_comment(db: Session, comment_id: int, user_id: int,comment: schemas.CommentCreate):
    db_comment = db.query(models.Comment).filter(models.Comment.id == comment_id).first()
    if not db_comment:
        raise HTTPException(status_code=404, detail="Commnet not found")
    if user_id != db_comment.author_id:
        raise HTTPException(status_code=403, detail="Do not have premission to change")
    if db_comment:
        for key, value in comment.dict(exclude_unset=True).items():
            setattr(db_comment, key, value)
        db.commit()
        db.refresh(db_comment)
    return db_comment

def delete_comment(db: Session, comment_id: int, user_id: int):
    comment = db.query(models.Comment).filter(models.Comment.id == comment_id).first()
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    if comment.author_id != user_id:
        raise HTTPException(status_code=403, detail="Do not have premission to delete")
    db.delete(comment)
    db.commit()


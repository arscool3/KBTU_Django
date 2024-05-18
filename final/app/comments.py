from fastapi import APIRouter, Depends, HTTPException

from pydantic import BaseModel
from sqlalchemy.orm import Session

from db import SessionLocal
import models

router = APIRouter(
    prefix="/comments",
    tags=["comments"],
    responses={404: {"description": "Not found"}}
)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class Comment(BaseModel):
    title: str


@router.get("/")
def get_comments(db: Session = Depends(get_db)):
    return db.query(models.Comment).all()


@router.post("/{users_id}/{post_id}")
def create_comment(comment: Comment, users_id: int, post_id: int, db: Session = Depends(get_db)):
    model = models.Comment()
    model.title = comment.title
    model.user_id = users_id
    model.post_id = post_id

    db.add(model)
    db.commit()

    return HTTPException(status_code=200, detail=f"Comment")


# update comment
@router.put("/{users_id}/{post_id}/{comment_id}")
def update_comment(comment: Comment, comment_id: int, users_id: int, post_id: int, db: Session = Depends(get_db)):
    comment_model = db.query(models.Comment).filter(models.Comment.id == comment_id) \
        .filter(models.Comment.post_id == post_id) \
        .filter(models.Comment.user_id == users_id).first()

    if not comment_model:
        raise HTTPException(status_code=404, detail=f"Comment not found")

    comment_model = models.Comment(**comment.dict())

    db.add(comment_model)
    db.commit()
    return HTTPException(status_code=200, detail=f"Comment successfully updated")


# delete comment
@router.delete("/{comment_id}")
def delete_comment(comment_id: int, db: Session = Depends(get_db)):
    db.query(models.Comment).filter(models.Comment.id == comment_id).delete()
    return HTTPException(status_code=200, detail="Successfully deleted")

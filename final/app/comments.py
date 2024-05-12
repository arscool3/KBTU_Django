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


@router.post("/")
def create_post(comment: Comment, db: Session = Depends(get_db)):
    model = models.Comment()
    model.title = Comment.title

    db.add(model)
    db.commit()

    return "Successfully created"

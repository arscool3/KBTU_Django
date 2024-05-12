from fastapi import APIRouter, Depends, HTTPException

from pydantic import BaseModel
from sqlalchemy.orm import Session

from db import SessionLocal
import models

router = APIRouter(
    prefix="/posts",
    tags=["posts"],
    responses={404: {"description": "Not found"}}
)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class Post(BaseModel):
    title: str
    content: str


@router.get("/")
def get_posts(db: Session = Depends(get_db)):
    return db.query(models.Post).all()


@router.post("/")
def create_post(post: Post, db: Session = Depends(get_db)):
    model = models.Post()
    model.title = post.title
    model.content = post.content

    db.add(model)
    db.commit()

    return "Successfully created"

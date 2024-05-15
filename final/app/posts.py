from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from db import SessionLocal
import models
from users import get_current_user

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
    description: str


@router.get("/")
def get_posts(db: Session = Depends(get_db)):
    return db.query(models.Post).all()


@router.post("/{user_id}")
def create_post(post: Post, user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    model = models.Post()
    model.title = post.title
    model.description = post.description
    model.user_id = user.get("id")

    db.add(model)
    db.commit()

    return "Successfully created"

from typing import List, Annotated

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session, joinedload

from db import SessionLocal
import models
from crud import AddDependency

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


# "get all posts"
@router.get("/")
def get_posts(db: Session = Depends(get_db)):
    return db.query(models.Post).all()


# "create post"
@router.post("/{user_id}")
# def create_post(post: Annotated[str, Depends(AddDependency.add_post)]):
#     return post
def create_post(post: Post, user_id: int, db: Session = Depends(get_db)):
    model = models.Post()
    model.title = post.title
    model.description = post.description
    model.user_id = user_id

    db.add(model)
    db.commit()

    return HTTPException(status_code=201, detail=f"Post")


# get post for user
@router.get("/{user_id}/posts")
def get_posts(user_id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.user_id == user_id).first()
    comments = db.query(models.Comment).filter(models.Comment.post_id == post.id).all()

    return post, comments


# get post
@router.get("/{post_id}")
def get_post(post_id: int, db: Session = Depends(get_db)):
    posts = db.query(models.Post).filter(models.Post.id == post_id).all()

    if not posts:
        raise HTTPException(status_code=404, detail="Post not found")

    return posts


# update post
@router.put("/{post_id}")
def update_post(post_id: int, given_post: Post, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()

    post.title = given_post.title
    post.description = given_post.description

    db.add(post)
    db.commit()

    return HTTPException(status_code=200, detail=f"Post")


# delete post
@router.delete("/{post_id}")
def delete_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="POst not found")

    db.query(models.Post).filter(models.Post.id == post_id).delete()
    db.commit()
    return HTTPException(status_code=204, detail="succesfully deleted")

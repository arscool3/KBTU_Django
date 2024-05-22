from typing import List

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import create_user, get_user, create_post, get_post, create_comment, get_comment, get_posts, get_users, \
    get_comments
from database import engine, SessionLocal
from schemas import UserSchema, PostSchema, CommentSchema
from models import Base

Base.metadata.create_all(bind=engine)
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/")
def create_user_api(user: UserSchema, db: Session = Depends(get_db)):
    return create_user(db, user.username, user.email)


@app.get("/users/{user_id}")
def get_user_api(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/posts/")
def create_post_api(post: PostSchema, db: Session = Depends(get_db)):
    return create_post(db, post.title, post.content, post.author_id)


@app.get("/posts/{post_id}")
def get_post_api(post_id: int, db: Session = Depends(get_db)):
    db_post = get_post(db, post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post


@app.post("/comments/")
def create_comment_api(comment: CommentSchema, db: Session = Depends(get_db)):
    return create_comment(db, comment.text, comment.post_id)


@app.get("/comments/{comment_id}")
def get_comment_api(comment_id: int, db: Session = Depends(get_db)):
    db_comment = get_comment(db, comment_id)
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return db_comment


@app.get("/users/", response_model=List[UserSchema])
def get_users_api(db: Session = Depends(get_db)):
    users = get_users(db)
    return users


@app.get("/posts/", response_model=List[PostSchema])
def get_posts_api(db: Session = Depends(get_db)):
    posts = get_posts(db)
    return posts


@app.get("/comments/", response_model=List[CommentSchema])
def get_comments_api(db: Session = Depends(get_db)):
    comments = get_comments(db)
    return comments

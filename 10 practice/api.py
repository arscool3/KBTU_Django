from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import sessionmaker, relationship, Session
from pydantic import BaseModel
from typing import Annotated
import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/")
def create_user(username: str, email: str, db: Annotated[Session, Depends(get_db)]):
    new_user = models.User(username=username, email=email)
    db.add(new_user)
    db.commit()
    return new_user

@app.get("/users/{user_id}")
def get_user(user_id: int, db: Annotated[Session, Depends(get_db)]):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/posts/")
def create_post(title: str, content: str, author_id: int, db: Annotated[Session, Depends(get_db)]):
    new_post = models.Post(title=title, content=content, author_id=author_id)
    db.add(new_post)
    db.commit()
    return new_post

@app.get("/posts/{post_id}")
def get_post(post_id: int, db: Annotated[Session, Depends(get_db)]):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@app.post("/comments/")
def create_comment(text: str, post_id: int, db: Annotated[Session, Depends(get_db)]):
    new_comment = models.Comment(text=text, post_id=post_id)
    db.add(new_comment)
    db.commit()
    return new_comment

@app.get("/comments/{comment_id}")
def get_comment(comment_id: int, db: Annotated[Session, Depends(get_db)]):
    comment = db.query(models.Comment).filter(models.Comment.id == comment_id).first()
    if comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return comment
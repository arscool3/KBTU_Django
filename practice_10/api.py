from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, Session
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    posts = relationship("Post", back_populates="author")

# class Post(Base):
#     __tablename__ = "posts"
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     content = Column(String)
#     author_id = Column(Integer, ForeignKey("users.id"))
#     author = relationship("User", back_populates="posts")

# class Comment(Base):
#     __tablename__ = "comments"
#     id = Column(Integer, primary_key=True, index=True)
#     text = Column(String)
#     post_id = Column(Integer, ForeignKey("posts.id"))
#     post = relationship("Post", back_populates="comments")

Base.metadata.create_all(bind=engine)

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

# class PostBase(BaseModel):
#     title: str
#     content: str
#     author_id: int

# class PostCreate(PostBase):
#     pass

# class Post(PostBase):
#     id: int

#     class Config:
#         orm_mode = True

# class CommentBase(BaseModel):
#     text: String
#     post_id: int

# class CommentCreate(CommentBase):
#     pass

# class Comment(CommentBase):
#     id: int

#     class Config:
#         orm_mode = True



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/")
def create_user(username: str, email: str, db: Annotated[Session, Depends(get_db)]):
    new_user = User(username=username, email=email)
    db.add(new_user)
    db.commit()
    return new_user

@app.get("/users/{user_id}")
def get_user(user_id: int, db: Annotated[Session, Depends(get_db)]):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/posts/")
def create_post(title: str, content: str, author_id: int, db: Annotated[Session, Depends(get_db)]):
    new_post = Post(title=title, content=content, author_id=author_id)
    db.add(new_post)
    db.commit()
    return new_post

@app.get("/posts/{post_id}")
def get_post(post_id: int, db: Annotated[Session, Depends(get_db)]):
    post = db.query(Post).filter(Post.id == post_id).first()
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@app.post("/comments/")
def create_comment(text: str, post_id: int, db: Annotated[Session, Depends(get_db)]):
    new_comment = Comment(text=text, post_id=post_id)
    db.add(new_comment)
    db.commit()
    return new_comment

@app.get("/comments/{comment_id}")
def get_comment(comment_id: int, db: Annotated[Session, Depends(get_db)]):
    comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return comment
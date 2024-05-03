from contextlib import contextmanager
from typing import Optional, List, Annotated

from fastapi import FastAPI, Depends, HTTPException, WebSocket
from sqlalchemy import select
from fastapi.middleware.cors import CORSMiddleware
import models as db
from entity import User, Comment, Post

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@contextmanager
def get_db():
    try:
        session = db.session
        yield session
        session.commit()
        session.close()
    except Exception:
        print('some exception')


@app.websocket("/posts/{post_id}/chat")
async def post_chat(websocket: WebSocket, post_id: int):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message received: {data}")


@app.get("/users/")
def get_users() -> list[User]:
    with get_db() as session:
        db_users = session.execute(select(db.User)).scalars().all()
        users = []
        for db_user in db_users:
            users.append(User.model_validate(db_user))
        return users


@app.get("/user")
def get_user(id: int) -> User:
    with get_db() as session:
        user = session.get(db.User, id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user


class AddDependency:

    @staticmethod
    def _add_model(db_model: type[db.User] | type[db.Post], pydantic_model: User | Post) -> None:
        with get_db() as session:
            session.add(db_model(**pydantic_model.model_dump()))

    @classmethod
    def add_user(cls, user: User) -> str:
        cls._add_model(db.User, user)
        return "User was added"

    @classmethod
    def add_post(cls, post: Post) -> str:
        cls._add_model(db.Post, post)
        return "Post was added"


@app.post("/users/")
def create_user(user: Annotated[str, Depends(AddDependency.add_user)]) -> str:
    return user


@app.post("/posts/")
def create_post(post: Annotated[str, Depends(AddDependency.add_post)]) -> str:
    return post


# @app.get("/posts/")
# def get_posts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
#     return db.query(Post).offset(skip).limit(limit).all()
#
#
# @app.get("/posts/{post_id}")
# def get_post(post_id: int, db: Session = Depends(get_db)):
#     post = db.query(Post).filter(Post.id == post_id).first()
#     if post is None:
#         raise HTTPException(status_code=404, detail="Post not found")
#     return post
#
#
# @app.put("/posts/{post_id}")
# def update_post(post_id: int, post_update: PostUpdate, db: Session = Depends(get_db)):
#     db_post = db.query(Post).filter(Post.id == post_id).first()
#     if db_post is None:
#         raise HTTPException(status_code=404, detail="Post not found")
#     for key, value in post_update.dict().items():
#         setattr(db_post, key, value)
#     db.commit()
#     db.refresh(db_post)
#     return db_post
#
#
# @app.delete("/posts/{post_id}")
# def delete_post(post_id: int, db: Session = Depends(get_db)):
#     db_post = db.query(Post).filter(Post.id == post_id).first()
#     if db_post is None:
#         raise HTTPException(status_code=404, detail="Post not found")
#     db.delete(db_post)
#     db.commit()
#     return {"message": "Post deleted successfully"}

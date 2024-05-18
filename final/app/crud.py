from fastapi import Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from db import SessionLocal
import models


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class Post(BaseModel):
    title: str
    description: str


class Comment(BaseModel):
    title: str


class AddDependency:

    @staticmethod
    def _add_model(db_model: type[models.Post] | type[models.Comment], pydantic_model: Post | Comment,
                   db: Session = Depends(get_db)) -> None:
        db_instance = db_model(**pydantic_model.dict())
        db.add(db_instance)
        db.commit()

    @classmethod
    def add_post(cls, post: Post) -> str:
        cls._add_model(models.Post, post)
        return "Post successfully added"

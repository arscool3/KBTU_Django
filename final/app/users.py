from fastapi import APIRouter, Depends, HTTPException

from pydantic import BaseModel
from sqlalchemy.orm import Session

from db import SessionLocal
import models

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}}
)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class User(BaseModel):
    username: str
    email: str
    password: str


@router.get("/")
def get_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()


@router.post("/")
def create_user(user: User, db: Session = Depends(get_db)):
    user_model = models.User()
    user_model.username = user.username
    user_model.email = user.email
    user_model.password = user.password

    db.add(user_model)
    db.commit()

    return "Successfully created"

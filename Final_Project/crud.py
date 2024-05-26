# crud.py
from sqlalchemy.orm import Session
import models
import schemas
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from fastapi import FastAPI, Depends, HTTPException, BackgroundTasks, status

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = models.User(
        username=user.username,
        email=user.email,
        full_name=user.username,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(db: Session, username: str, password: str):
    user = get_user_by_username(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def get_object(db: Session, model, obj_id: int):
    return db.query(model).filter(model.id == obj_id).first()

def get_objects(db: Session, model, skip: int = 0, limit: int = 10):
    return db.query(model).offset(skip).limit(limit).all()

def create_object(db: Session, model, obj_in):
    db_obj = model(**obj_in.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_object(db: Session, model, obj_id: int, obj_in):
    db_obj = get_object(db, model, obj_id)
    if not db_obj:
        return None
    for key, value in obj_in.dict().items():
        setattr(db_obj, key, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_object(db: Session, model, obj_id: int):
    db_obj = get_object(db, model, obj_id)
    if not db_obj:
        return None
    db.delete(db_obj)
    db.commit()
    return db_obj



def borrow_book(db: Session, book_id: int, member_id: int) -> bool:
    # Check if both book and member exist
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        return False

    member = db.query(models.Member).filter(models.Member.id == member_id).first()
    if not member:
        return False

    # Check if the book is available for borrowing
    if book.is_available_for_borrowing:
        # Update book status
        book.is_available_for_borrowing = False
        db.commit()

        # Create a loan record
        loan = models.Loan(book_id=book_id, member_id=member_id)
        db.add(loan)
        db.commit()
        return True

    return False



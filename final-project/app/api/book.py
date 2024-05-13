from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies.auth import get_current_user
from app.dependencies.database import get_db
from app.models.book import Book
from app.models.user import User
from app.schemas.book import BookCreate
from app.tasks.background_tasks import add_book

router = APIRouter()


@router.post("/books/")
async def create_book(book_data: BookCreate, current_user: User = Depends(get_current_user),
                      db: Session = Depends(get_db)):
    db_book = Book(title=book_data.title, author_id=book_data.author_id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    add_book.send()
    return db_book



@router.get("/books/{book_id}/")
async def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book


@router.get("/books/")
async def read_books(db: Session = Depends(get_db)):
    return db.query(Book).all()


@router.put("/books/{book_id}/")
async def update_book(book_id: int, book_data: BookCreate, current_user: User = Depends(get_current_user),
                      db: Session = Depends(get_db)):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    if db_book.author_id != current_user.id:
        raise HTTPException(status_code=403, detail="You can only update your own books")
    for key, value in book_data.dict().items():
        setattr(db_book, key, value)
    db.commit()
    db.refresh(db_book)
    return db_book


@router.delete("/books/{book_id}/")
async def delete_book(book_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    if db_book.author_id != current_user.id:
        raise HTTPException(status_code=403, detail="You can only delete your own books")
    db.delete(db_book)
    db.commit()
    return db_book

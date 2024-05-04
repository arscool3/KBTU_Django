from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
from schemas import BookCreate, AuthorCreate, GenreCreate
from typing import List
from crud import create_book, create_author, create_genre, get_book, get_author, get_genre

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.get("/books/{book_id}", response_model=models.Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = get_book(db, book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@app.get("/authors/{author_id}", response_model=models.Author)
def read_author(author_id: int, db: Session = Depends(get_db)):
    db_author = get_author(db, author_id)
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return db_author

@app.get("/genres/{genre_id}", response_model=models.Genre)
def read_genre(genre_id: int, db: Session = Depends(get_db)):
    db_genre = get_genre(db, genre_id)
    if db_genre is None:
        raise HTTPException(status_code=404, detail="Genre not found")
    return db_genre


@app.post("/books/", response_model=models.Book)
def create_book_api(book: BookCreate, db: Session = Depends(get_db)):
    return create_book(db=db, book=book)

@app.post("/authors/", response_model=models.Author)
def create_author_api(author: AuthorCreate, db: Session = Depends(get_db)):
    return create_author(db=db, author=author)

@app.post("/genres/", response_model=models.Genre)
def create_genre_api(genre: GenreCreate, db: Session = Depends(get_db)):
    return create_genre(db=db, genre=genre)

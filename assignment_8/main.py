from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Book(BaseModel):
    id: int
    title: str
    author: str

books: List[Book] = []

@app.get("/books", response_model=List[Book])
def get_books():
    return books

@app.post("/books", response_model=Book)
def create_book(book: Book):
    if any(b.id == book.id for b in books):
        raise HTTPException()
    books.append(book)
    return book

@app.get("/books/{id}", response_model=Book)
def update_book(book_id: int, updated_book: Book):
    for i, book in enumerate(books):
        if book.id == book_id:
            books[i] = updated_book
            return updated_book
        raise HTTPException()

@app.delete("/books/{id}", response_model=Book)
def delete_book(book_id: int):
    for i, book in enumerate(books):
        if book.id == book_id:
            books.pop(i)
        raise HTTPException()

#uvicorn main:app --reload
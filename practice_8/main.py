from pydantic import BaseModel

class Book(BaseModel):
    title: str
    author: str
from fastapi import FastAPI
from typing import List

app = FastAPI()

books = []

@app.get("/books", response_model=List[Book])
async def get_books():
    return books

@app.post("/books", response_model=Book)
async def create_book(book: Book):
    books.append(book)
    return book

@app.put("/books/{book_id}", response_model=Book)
async def update_book(book_id: int, book: Book):
    if book_id < len(books):
        books[book_id] = book
        return books[book_id]
    else:
        return {"error": "Book not found"}

@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    if book_id < len(books):
        books.pop(book_id)
        return {"message": "Book deleted"}
    else:
        return {"error": "Book not found"}

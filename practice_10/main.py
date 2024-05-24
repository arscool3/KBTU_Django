from pydantic import BaseModel
from typing import List, Optional

from fastapi import FastAPI, Depends, HTTPException
from typing import List


class Publisher(BaseModel):
    name: str
    city: str

class Author(BaseModel):
    name: str
    birth_year: int

class Book(BaseModel):
    title: str
    author_id: int
    publisher_id: int
    author: Optional[Author] = None
    publisher: Optional[Publisher] = None

app = FastAPI()

books_db = []
authors_db = []
publishers_db = []

def get_book_by_id(book_id: int):
    for book in books_db:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

def get_author_by_id(author_id: int):
    for author in authors_db:
        if author["id"] == author_id:
            return author
    raise HTTPException(status_code=404, detail="Author not found")

def get_publisher_by_id(publisher_id: int):
    for publisher in publishers_db:
        if publisher["id"] == publisher_id:
            return publisher
    raise HTTPException(status_code=404, detail="Publisher not found")

@app.post("/books/", response_model=Book)
async def create_book(book: Book):
    books_db.append(book.dict())
    return book

@app.get("/books/{book_id}", response_model=Book)
async def read_book(book_id: int, book: Book = Depends(get_book_by_id)):
    return book

@app.post("/authors/", response_model=Author)
async def create_author(author: Author):
    authors_db.append(author.model_dump())
    return author

@app.get("/authors/{author_id}", response_model=Author)
async def read_author(author_id: int, author: Author = Depends(get_author_by_id)):
    return author

@app.post("/publishers/", response_model=Publisher)
async def create_publisher(publisher: Publisher):
    publishers_db.append(publisher.model_dump())
    return publisher

@app.get("/publishers/{publisher_id}", response_model=Publisher)
async def read_publisher(publisher_id: int, publisher: Publisher = Depends(get_publisher_by_id)):
    return publisher

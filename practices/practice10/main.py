from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Author(BaseModel):
    id: int
    name: str


class Book(BaseModel):
    id: int
    title: str
    author_id: int


class Publisher(BaseModel):
    id: int
    name: str


authors = [
    Author(id=1, name="John Doe"),
    Author(id=2, name="Jane Smith"),
]

publishers = [
    Publisher(id=1, name="Publisher A"),
    Publisher(id=2, name="Publisher B"),
]

books = [
    Book(id=1, title="Book 1", author_id=1),
    Book(id=2, title="Book 2", author_id=1),
    Book(id=3, title="Book 3", author_id=2),
]


@app.get("/authors/{author_id}", response_model=Author)
def get_author(author_id: int):
    for author in authors:
        if author.id == author_id:
            return author
    raise HTTPException(status_code=404, detail="Author not found")


@app.get("/books/", response_model=List[Book])
def get_books():
    return books


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.get("/authors/{author_id}/books", response_model=List[Book])
def get_books_by_author(author_id: int):
    author_books = [book for book in books if book.author_id == author_id]
    if author_books:
        return author_books
    else:
        raise HTTPException(status_code=404, detail="Author has no books")


@app.post("/authors/", response_model=Author)
def create_author(author: Author):
    authors.append(author)
    return author


@app.post("/books/", response_model=Book)
def create_book(book: Book):
    books.append(book)
    return book


@app.post("/publishers/", response_model=Publisher)
def create_publisher(publisher: Publisher):
    publishers.append(publisher)
    return publisher

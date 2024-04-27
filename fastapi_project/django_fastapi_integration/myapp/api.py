from fastapi import FastAPI, HTTPException
from django.shortcuts import get_object_or_404
from .models import Author, Book, Reader

app = FastAPI()

@app.get("/authors/{author_id}")
async def read_author(author_id: int):
    author = get_object_or_404(Author, id=author_id)
    return author

@app.post("/authors/")
async def create_author(author: Author):
    author.save()
    return author

@app.get("/books/{book_id}")
async def read_book(book_id: int):
    book = get_object_or_404(Book, id=book_id)
    return book

@app.post("/books/")
async def create_book(book: Book):
    book.save()
    return book

@app.get("/readers/{reader_id}")
async def read_reader(reader_id: int):
    reader = get_object_or_404(Reader, id=reader_id)
    return reader

@app.post("/readers/")
async def create_reader(reader: Reader):
    reader.save()
    return reader

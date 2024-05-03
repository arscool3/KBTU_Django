import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'accio_book.settings')
django.setup()

from my_app.models import Book
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class BookCreate(BaseModel):
    title: str
    author: str
    genre: str

@app.post("/api/books/")
async def create_book(book_data: BookCreate):
    book = Book.objects.create(title=book_data.title, author=book_data.author, genre=book_data.genre)
    return {"id": book.id, "title": book.title, "author": book.author, "genre": book.genre}

@app.get("/api/books/")
async def get_books():
    books = Book.objects.all()
    serialized_books = [{"id": book.id, "title": book.title, "author": book.author, "genre": book.genre} for book in books]
    return serialized_books

@app.get("/api/books/{book_id}/")
async def get_book(book_id: int):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return JsonResponse({"error": "Book not found"}, status=404)
    return {"id": book.id, "title": book.title, "author": book.author, "genre": book.genre}

@app.delete("/api/books/{book_id}/")
async def delete_book(book_id: int):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return JsonResponse({"error": "Book not found"}, status=404)
    book.delete()
    return {"message": "Book deleted successfully"}

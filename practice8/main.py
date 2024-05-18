from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


app = FastAPI()

shops = []
products = []

class Book(BaseModel):
    name: str
    author: str

class Category(BaseModel):
    name: str
    book_id: int

books = []

categories = []

@app.post("/books/")
async def create_book(book: Book):
    books.append(book)
    return {"message": "book created successfully"}

@app.get("/books/", response_model=List[Book])
async def get_books():
    return books

@app.get("/books/{index}", response_model=Book)
async def get_book_by_index(index: int):
    try:
        return books[index]
    except IndexError:
        raise HTTPException(status_code=404, detail="book not found")

@app.put("/books/{index}")
async def update_book(index: int, book: Book):
    try:
        books[index] = book
        return {"message": "book updated successfully"}
    except IndexError:
        raise HTTPException(status_code=404, detail="book not found")

@app.delete("/books/{index}")
async def delete_book(index: int):
    try:
        del books[index]
        return {"message": "book deleted successfully"}
    except IndexError:
        raise HTTPException(status_code=404, detail="book not found")

@app.post("/categories/")
async def create_category(category: Category):
    categories.append(category)
    return {"message": "Category created successfully"}

@app.get("/categories/", response_model=List[Category])
async def get_categories():
    return categories

@app.get("/books/{book_id}/categories", response_model=List[Category])
async def get_categories_for_book(book_id: int):
    return [category for category in categories if category.book_id == book_id]

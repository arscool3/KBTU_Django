from django.db import models
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Author(BaseModel):
    id: int
    name: str

    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    books = relationship("Book", back_populates="author")

class Book(BaseModel):
    id: int
    title: str
    author_id: int
    category: str
    publication_date: str

    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author_id = Column(Integer, ForeignKey("authors.id"))

    author = relationship("Author", back_populates="books")

class Category(BaseModel):
    id: int
    name: str

class Borrower(BaseModel):
    id: int
    name: str

class BorrowedBook(BaseModel):
    id: int
    book_id: int
    borrower_id: int
    borrowed_date: str
    due_date: str

class User(BaseModel):
    id: int
    username: str
    email: str
    password: str
    is_active: bool
    is_staff: bool


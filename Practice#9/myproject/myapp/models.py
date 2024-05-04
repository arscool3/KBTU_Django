from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

DATABASE_URL = "sqlite:///./bookstore.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Models with Relationships
class Publisher(Base):
    __tablename__ = "publishers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    books = relationship("Book", back_populates="publisher")

class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    books = relationship("Book", back_populates="author")

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True)
    author_id = Column(Integer, ForeignKey("authors.id"))
    publisher_id = Column(Integer, ForeignKey("publishers.id"))

    author = relationship("Author", back_populates="books")
    publisher = relationship("Publisher", back_populates="books")

# Pydantic Models
class PublisherCreate(BaseModel):
    name: str

class AuthorCreate(BaseModel):
    name: str

class BookCreate(BaseModel):
    title: str
    author_id: int
    publisher_id: int

class AuthorResponse(BaseModel):
    id: int
    name: str
    books: List[str] = []  # Book titles
    class Config:
        orm_mode = True

class PublisherResponse(BaseModel):
    id: int
    name: str
    books: List[str] = []  # Book titles
    class Config:
        orm_mode = True

class BookResponse(BaseModel):
    id: int
    title: str
    author_id: int
    publisher_id: int
    class Config:
        orm_mode = True

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base.metadata.create_all(bind=engine)

@app.post("/publishers/", response_model=PublisherResponse)
def create_publisher(publisher: PublisherCreate, db: Session = Depends(get_db)):
    new_publisher = Publisher(name=publisher.name)
    db.add(new_publisher)
    db.commit()
    db.refresh(new_publisher)
    return new_publisher

@app.get("/publishers/", response_model=List[PublisherResponse])
def get_publishers(db: Session = Depends(get_db)):
    publishers = db.query(Publisher).all()
    return publishers

@app.post("/authors/", response_model=AuthorResponse)
def create_author(author: AuthorCreate, db: Session = Depends(get_db)):
    new_author = Author(name=author.name)
    db.add(new_author)
    db.commit()
    db.refresh(new_author)
    return new_author

@app.get("/authors/", response_model=List[AuthorResponse])
def get_authors(db: Session = Depends(get_db)):
    authors = db.query(Author).all()
    return authors

@app.post("/books/", response_model=BookResponse)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    new_book = Book(title=book.title, author_id=book.author_id, publisher_id=book.publisher_id)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

@app.get("/books/", response_model=List[BookResponse])
def get_books(db: Session = Depends(get_db)):
    books = db.query(Book).all()
    return books


from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from pydantic import BaseModel

from models import Author, Book, Publisher, Base
from fastapi import WebSocket

DATABASE_URL = "postgresql://postgres:Ayef1407_@localhost/djangopractice"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")



class AuthorIn(BaseModel):
    name: str


class BookIn(BaseModel):
    title: str
    author_id: int
    publisher_id: int


class PublisherIn(BaseModel):
    name: str


# Routes
@app.post("/authors/")
def create_author(author_in: AuthorIn):
    try:
        print("Received author name:", author_in.name)  # Отладочный вывод
        db = SessionLocal()
        author = Author(name=author_in.name)
        db.add(author)
        db.commit()
        db.refresh(author)
        db.close()
        return author
    except Exception as e:
        print("An error occurred while creating author:", e)
        raise HTTPException(status_code=500, detail="Internal Server Error")



@app.get("/authors/{author_id}")
def get_author(author_id: int):
    db = SessionLocal()
    author = db.query(Author).filter(Author.id == author_id).first()
    db.close()
    if author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return author


@app.post("/books/")
def create_book(book_in: BookIn):
    try:
        print("Received book:", book_in.title, book_in.author_id, book_in.publisher_id)  # Отладочный вывод
        db = SessionLocal()
        book = Book(title=book_in.title, author_id=book_in.author_id, publisher_id=book_in.publisher_id)
        db.add(book)
        db.commit()
        db.refresh(book)
        db.close()
        return book
    except Exception as e:
        print("An error occurred while creating book:", e)
        raise HTTPException(status_code=500, detail="Internal Server Error")


@app.get("/books/{book_id}")
def get_book(book_id: int):
    db = SessionLocal()
    book = db.query(Book).filter(Book.id == book_id).first()
    db.close()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@app.post("/publishers/")
def create_publisher(publisher_in: PublisherIn):
    try:
        print("Received publisher name:", publisher_in.name)  # Отладочный вывод
        db = SessionLocal()
        publisher = Publisher(name=publisher_in.name)
        db.add(publisher)
        db.commit()
        db.refresh(publisher)
        db.close()
        return publisher
    except Exception as e:
        print("An error occurred while creating publisher:", e)
        raise HTTPException(status_code=500, detail="Internal Server Error")


@app.get("/publishers/{publisher_id}")
def get_publisher(publisher_id: int):
    db = SessionLocal()
    publisher = db.query(Publisher).filter(Publisher.id == publisher_id).first()
    db.close()
    if publisher is None:
        raise HTTPException(status_code=404, detail="Publisher not found")
    return publisher

from fastapi import FastAPI, Depends, HTTPException, WebSocket
from fastapi.responses import HTMLResponse
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship

app = FastAPI()

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    books = relationship("Book", back_populates="author")


class Publisher(Base):
    __tablename__ = "publishers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    books = relationship("Book", back_populates="publisher")


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author_id = Column(Integer, ForeignKey("authors.id"))
    publisher_id = Column(Integer, ForeignKey("publishers.id"))

    author = relationship("Author", back_populates="books")

    publisher = relationship("Publisher", back_populates="books")


Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_author(db: Session, author_id: int):
    return db.query(Author).filter(Author.id == author_id).first()


def create_author(db: Session, name: str):
    db_author = Author(name=name)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


def get_publisher(db: Session, publisher_id: int):
    return db.query(Publisher).filter(Publisher.id == publisher_id).first()


def create_publisher(db: Session, name: str):
    db_publisher = Publisher(name=name)
    db.add(db_publisher)
    db.commit()
    db.refresh(db_publisher)
    return db_publisher

def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()


def create_book(db: Session, title: str, author_id: int, publisher_id: int):
    db_book = Book(title=title, author_id=author_id, publisher_id=publisher_id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


@app.post("/authors/")
def create_author_route(name: str, db: Session = Depends(get_db)):
    return create_author(db, name)


@app.get("/authors/{author_id}")
def read_author(author_id: int, db: Session = Depends(get_db)):
    author = get_author(db, author_id)
    if author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return author


@app.post("/publishers/")
def create_publisher_route(name: str, db: Session = Depends(get_db)):
    return create_publisher(db, name)


@app.get("/publishers/{publisher_id}")
def read_publisher(publisher_id: int, db: Session = Depends(get_db)):
    publisher = get_publisher(db, publisher_id)
    if publisher is None:
        raise HTTPException(status_code=404, detail="Publisher not found")
    return publisher


@app.post("/books/")
def create_book_route(title: str, author_id: int, publisher_id: int, db: Session = Depends(get_db)):
    return create_book(db, title, author_id, publisher_id)


@app.get("/books/{book_id}")
def read_book(book_id: int, db: Session = Depends(get_db)):
    book = get_book(db, book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")

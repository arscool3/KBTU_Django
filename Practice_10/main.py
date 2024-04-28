from databases import Database
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from fastapi import HTTPException
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from fastapi import FastAPI
from models import Book, Author, Category

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/postgres"

database = Database(DATABASE_URL)
Base = declarative_base()


class AuthorDB(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer, nullable=True)


class CategoryDB(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)


class BookDB(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author_id = Column(Integer, ForeignKey('authors.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))
    page_count = Column(Integer)
    author = relationship("AuthorDB")
    category = relationship("CategoryDB")


engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.post("/books/")
async def create_book(book: Book):
    async with Session(engine) as session:
        db_book = BookDB(**book.dict())
        session.add(db_book)
        await session.commit()
        return db_book


@app.get("/books/")
async def read_books():
    async with Session(engine) as session:
        result = await session.execute(select(BookDB))
        books = result.scalars().all()
        return books


@app.get("/books/{book_id}")
async def read_book(book_id: int):
    async with Session(engine) as session:
        result = await session.execute(select(BookDB).where(BookDB.id == book_id))
        book = result.scalars().first()
        if book is None:
            raise HTTPException(status_code=404, detail="Book not found")
        return book
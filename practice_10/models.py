import sqlalchemy as sa

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, Mapped, mapped_column, relationship
from sqlalchemy.ext.declarative import declarative_base

url = 'postgresql://postgres:postgres@localhost/postgres'
engine = create_engine(url)
session = Session(engine)

Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String)
    books = relationship("Book", back_populates="author")

class Genre(Base):
    __tablename__ = 'genres'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String)
    books = relationship("BookGenre", back_populates="genre")

class Book(Base):
    __tablename__ = 'books'
    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String)
    author_id = sa.Column(sa.Integer, sa.ForeignKey('authors.id'))
    author = relationship("Author", back_populates="books")
    genres = relationship("BookGenre", back_populates="book")

class BookGenre(Base):
    __tablename__ = 'book_genres'
    id = sa.Column(sa.Integer, primary_key=True)
    book_id = sa.Column(sa.Integer, sa.ForeignKey('books.id'))
    genre_id = sa.Column(sa.Integer, sa.ForeignKey('genres.id'))
    book = relationship("Book", back_populates="genres")
    genre = relationship("Genre", back_populates="books")
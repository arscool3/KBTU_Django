from sqlalchemy import Column, Integer, String,JSON,func
from database import Base

from typing import Annotated
import sqlalchemy
from sqlalchemy.orm import mapped_column, Mapped, relationship

from datetime import datetime
_id = Annotated[int, mapped_column(sqlalchemy.Integer, primary_key=True)]


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    fullname = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    
class UserLogin(Base):
    __tablename__ = 'user_logins'
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)

# genres and books relationship, author and books relationship, user and reviews relationship
#reviews and books relationship, quote and author
class Goodreads:
    id: Mapped[_id]
    name: Mapped[str]
    description: Mapped[str]

class Genre(Base,Goodreads):
    __tablename__ = 'genres'
    books: Mapped['Book'] = relationship("Book", back_populates='genre')

class Book(Base,Goodreads):
    __tablename__ = 'books'
    author_id: Mapped[int] = mapped_column(sqlalchemy.ForeignKey('authors.id'))
    author: Mapped['Author'] = relationship("Author", back_populates='books')
    genre_id: Mapped[int] = mapped_column(sqlalchemy.ForeignKey('genres.id'))
    genre: Mapped['Genre'] = relationship("Genre",back_populates='books')
    bookreviews: Mapped['BookReview'] = relationship("BookReview", back_populates='book')

class Author(Base,Goodreads):
    __tablename__ = 'authors'
    books: Mapped[Book] = relationship("Book", back_populates='author')
    quotes:Mapped['Quote']=relationship("Quote",back_populates='author')

class Quote(Base):
    __tablename__='quotes'
    id: Mapped[_id]
    description: Mapped[str]    
    author_id: Mapped[int] = mapped_column(sqlalchemy.ForeignKey('authors.id'))
    author: Mapped['Author'] = relationship("Author", back_populates='quotes') 

class BookReview(Base):
    __tablename__='bookreviews'
    id: Mapped[_id]
    review: Mapped[str] 
    rating:Mapped[int]
    book_id: Mapped[int]=mapped_column(sqlalchemy.ForeignKey('books.id'))
    book: Mapped[Book] = relationship("Book", back_populates='bookreviews')

class AccessLogJournal(Base):
    __tablename__ = 'access_log_journal'
    id: Mapped[_id]
    data = Column(JSON, nullable=True)
    method: Mapped[str]
    request: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

class Film(Base):
    __tablename__ = 'film'
    id:Mapped[_id]
    name:Mapped[str]
    director:Mapped[str]
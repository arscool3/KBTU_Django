# models.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, ForeignKey, Date

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    email = Column(String, unique=True, index=True)
    full_name = Column(String)


class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    books = relationship("Book", back_populates="author")

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author_id = Column(Integer, ForeignKey('authors.id'))
    genre_id = Column(Integer, ForeignKey('genres.id'))
    publisher_id = Column(Integer, ForeignKey('publishers.id'))
    author = relationship("Author", back_populates="books")
    genre = relationship("Genre", back_populates="books")
    publisher = relationship("Publisher", back_populates="books")
    reviews = relationship("Review", back_populates="book")

class Genre(Base):
    __tablename__ = 'genres'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    books = relationship("Book", back_populates="genre")

class Library(Base):
    __tablename__ = 'libraries'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location = Column(String)
    staff = relationship("Staff", back_populates="library")
    sections = relationship("Section", back_populates="library")

class Loan(Base):
    __tablename__ = 'loans'

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    member_id = Column(Integer, ForeignKey('members.id'))
    loan_date = Column(Date)
    return_date = Column(Date)
    book = relationship("Book")
    member = relationship("Member", back_populates="loans")

class Member(Base):
    __tablename__ = 'members'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    loans = relationship("Loan", back_populates="member")

class Publisher(Base):
    __tablename__ = 'publishers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    books = relationship("Book", back_populates="publisher")

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, index=True)
    rating = Column(Integer)
    book_id = Column(Integer, ForeignKey('books.id'))
    book = relationship("Book", back_populates="reviews")

class Section(Base):
    __tablename__ = 'sections'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    library_id = Column(Integer, ForeignKey('libraries.id'))
    library = relationship("Library", back_populates="sections")

class Staff(Base):
    __tablename__ = 'staff'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    library_id = Column(Integer, ForeignKey('libraries.id'))
    library = relationship("Library", back_populates="staff")
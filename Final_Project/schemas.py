from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class UserBase(BaseModel):
    username: str
    email: str
    full_name: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class AuthorBase(BaseModel):
    name: str

class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    id: int
    books: List['Book'] = []

    class Config:
        orm_mode = True

class BookBase(BaseModel):
    title: str
    author_id: int
    genre_id: int
    publisher_id: int

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int

    class Config:
        orm_mode = True

class GenreBase(BaseModel):
    name: str

class GenreCreate(GenreBase):
    pass

class Genre(GenreBase):
    id: int
    books: List[Book] = []

    class Config:
        orm_mode = True

class LibraryBase(BaseModel):
    name: str
    location: str

class LibraryCreate(LibraryBase):
    pass

class Library(LibraryBase):
    id: int

    class Config:
        orm_mode = True

class LoanBase(BaseModel):
    book_id: int
    member_id: int
    loan_date: date
    return_date: Optional[date] = None

class LoanCreate(LoanBase):
    pass

class Loan(LoanBase):
    id: int

    class Config:
        orm_mode = True

class MemberBase(BaseModel):
    name: str

class MemberCreate(MemberBase):
    pass

class Member(MemberBase):
    id: int
    loans: List[Loan] = []

    class Config:
        orm_mode = True

class PublisherBase(BaseModel):
    name: str

class PublisherCreate(PublisherBase):
    pass

class Publisher(PublisherBase):
    id: int

    class Config:
        orm_mode = True

class ReviewBase(BaseModel):
    content: str
    rating: int
    book_id: int

class ReviewCreate(ReviewBase):
    pass

class Review(ReviewBase):
    id: int

    class Config:
        orm_mode = True

class SectionBase(BaseModel):
    name: str
    library_id: int

class SectionCreate(SectionBase):
    pass

class Section(SectionBase):
    id: int

    class Config:
        orm_mode = True

class StaffBase(BaseModel):
    name: str
    library_id: int

class StaffCreate(StaffBase):
    pass

class Staff(StaffBase):
    id: int

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

from pydantic import BaseModel, Field, EmailStr

class UserSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)
    class Config:
        from_attributes = True

class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)
    class Config:
        from_attributes = True

class Base(BaseModel):
    name: str
    description:str
    class Config:
        from_attributes = True

class Author(Base):
    id:int

class CreateAuthor(Base):
    pass

class Genre(Base):
    id:int

class CreateGenre(Base):
    pass

class Book(Base):
    id: int
    author: Author
    genre: Genre


class CreateBook(Base):
    author_id:int
    genre_id:int

class BaseQuote(BaseModel):
    description:str

    class Config:
        from_attributes = True  

class Quote(BaseQuote):
    id:int
    author:Author

class CreateQuote(BaseQuote):
    author_id:int

class BaseBookReview(BaseModel):
    review:str
    rating:int

    class Config:
        from_attributes = True  

class BookReview(BaseBookReview):
    id:int


class CreateBookReview(BaseBookReview):
    book_id: int
    
class Employee(BaseModel):
    name: str
    age: int
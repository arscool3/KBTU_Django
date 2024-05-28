from pydantic import BaseModel


class BookCreate(BaseModel):
    title: str
    author_id: int
    genre_id: int


class AuthorCreate(BaseModel):
    name: str


class GenreCreate(BaseModel):
    name: str

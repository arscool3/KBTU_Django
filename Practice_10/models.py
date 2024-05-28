from pydantic import BaseModel
from typing import Optional


class Author(BaseModel):
    name: str
    age: Optional[int] = None


class Category(BaseModel):
    name: str


class Book(BaseModel):
    title: str
    author: Author
    category: Category
    page_count: int
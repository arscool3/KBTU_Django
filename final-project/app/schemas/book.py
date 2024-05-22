from pydantic import BaseModel
from typing import Optional

class BookBase(BaseModel):
    title: str
    author_id: int

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int

    class Config:
        orm_mode = True

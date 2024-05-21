from pydantic import BaseModel
from typing import List, Optional

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    class Config:
        orm_mode = True


class PaperBase(BaseModel):
    title: str
    abstract: str
    fields: List[int] = []
    file_path: str

class PaperCreate(PaperBase):
    pass

class Paper(PaperBase):
    id: int
    author_id: int
    tags: List[int] = []
    class Config:
        orm_mode = True

class CommentBase(BaseModel):
    content: str

class CommentCreate(CommentBase):
    paper_id: int

class Comment(CommentBase):
    id: int
    author_id: int
    paper_id: int
    class Config:
        orm_mode = True

class Tag(BaseModel):
    id: int
    name: str
    class Config:
        orm_mode = True

class Field(BaseModel):
    id: int
    name: str
    class Config:
        orm_mode = True


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
    content: str
    field_id: int

class PaperCreate(PaperBase):
    pass

class Paper(PaperBase):
    id: int
    author_id: int
    tags: List[str] = []
    fields: List[str] = []
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


class FavoriteBase(BaseModel):
    paper_id: int

class FavoriteCreate(FavoriteBase):
    pass

class Favorite(FavoriteBase):
    id: int
    user_id: int
    papers: List[str] = []
    class Config:
        orm_mode = True


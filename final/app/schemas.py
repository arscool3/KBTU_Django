from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
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


class PaperBase(BaseModel):
    title: str
    abstract: str
    fields: List[int] = []
    tags: List[int] = []
    file_path: str

class PaperCreate(PaperBase):
    pass

class PaperUpdate(BaseModel):
    title: Optional[str] = None
    abstract: Optional[str] = None
    tags: Optional[List[int]] = None
    fields: Optional[List[int]] = None
    file_path: Optional[str] = None


class Paper(PaperBase):
    id: int
    author_id: int
    uploaded_at: datetime
    fields: List[Field] = []
    tags: List[Tag] = []
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
    created_at: datetime
    class Config:
        orm_mode = True

class FavoriteCreate(BaseModel):
    paper_id: int

class Favorite(FavoriteCreate):
    id: int
    user_id: int
    class Config:
        orm_mode = True

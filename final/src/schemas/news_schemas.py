from pydantic import BaseModel, Field
from models import User
from datetime import datetime


class NewsBase(BaseModel):
    author_id: int = Field(default=None, foreign_key="users.id")
    title: str
    text: str
    date: datetime

class NewsCreate(NewsBase):
    pass

class News(NewsBase):
    id: int

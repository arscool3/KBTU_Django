from pydantic import BaseModel
from typing import Optional

class ReviewBase(BaseModel):
    content: str
    user_id: int
    book_id: int

class ReviewCreate(ReviewBase):
    pass

class Review(ReviewBase):
    id: int

    class Config:
        orm_mode = True

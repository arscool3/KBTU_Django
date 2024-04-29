from pydantic import BaseModel
from datetime import datetime


class Base(BaseModel):

    class Config:
        from_attributes = True


class Category(Base):
    name: str
    photo_url: str


class Product(Base):
    name: str
    price: int
    description: str
    photo_url: str
    category_id: int
    
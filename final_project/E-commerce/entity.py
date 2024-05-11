import datetime
from typing import Optional
from pydantic import BaseModel, Field

class User(BaseModel):
    user_id: int
    username: str
    password: str

class Product(BaseModel):
    product_id: int
    name: str
    description: str
    category_id: int
    brand_id: Optional[int] = None


class Category(BaseModel):
    category_id: int
    name: str


class Brand(BaseModel):
    brand_id: int
    name: str


class Review(BaseModel):
    review_id: int
    product_id: int
    user_id: int
    rating: float
    title: str
    description: str


class Order(BaseModel):
    order_id: int
    user_id: int
    # placed_at: datetime
    status: str  
    items: list[dict]  


class Token(BaseModel):
    access_token: str
    token_type: str

class DataToken(BaseModel):
    user_id: int

import datetime
from typing import Optional
from pydantic import BaseModel, Field

class User(BaseModel):
    username: str
    password: str

class Product(BaseModel):
    name: str
    description: str
    category_id: int
    brand_id: int


class ProductUpdate(BaseModel):
    name: str
    description: str

class Category(BaseModel):
    name: str


class Brand(BaseModel):
    name: str


class Review(BaseModel):
    product_id: int
    user_id: int
    rating: float
    name: str
    description: str


class Order(BaseModel):
    user_id: int
    product_id: int
    status: str  


class Token(BaseModel):
    access_token: str
    token_type: str

class DataToken(BaseModel):
    user_id: int

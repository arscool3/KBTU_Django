from pydantic import BaseModel
from datetime import datetime


class Base(BaseModel):

    class Config:
        from_attributes = True

class User(Base):
   
    username: str

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

class Cart(Base):
    user_id: int
    
class CartItem(Base):
    product_id: int
    cart_id: int
    quantity: int

class Store(Base):
    store_name: str
    user_id: int

class StoreItem(Base):
    store_id: int
    product_id: int
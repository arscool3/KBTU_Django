from pydantic import BaseModel
from datetime import datetime

class Base(BaseModel):

    class Config:
        from_attributes = True

class Food(Base):
    id:int
    category_id: int
    name: str
    description: str
    price: int

class Order(Base):
    reservation: int
    created_at: str
    status: str
    pay:bool
    # total: int
class CreateOrder(Base):
    reservation: int

class OrderItem(Base):
    food_id: int
    quantity: int

class Category(Base):
    id: int
    name:str

    
class PaymentStatus(Base):
    status_code: str
    reservation_id: int

class History(Base):
    reservation: int
    datetime: datetime
    total: int

class CreateHistory(Base):
    reservation: int

class HistoryItem(Base):
    food_id: int
    quantity: int
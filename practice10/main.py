from typing import List, Optional, Dict
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

app = FastAPI()
class Custmoer(BaseModel):
    id: int
    username: str

class Book(BaseModel):
    id: int
    name: str
    price: float
    owner_id: int

class Order(BaseModel):
    id: int
    books: List[Book]
    user_id: int

customer_db: Dict[int, User] = {}
books_db: Dict[int, Book] = {}
orders_db: Dict[int, Order] = {}


@app.post("/books/", response_model=Book)
def create_Book(Book: Book):
    books_db[Book.id] = Book
    return Book

# GET query for retrieving an Book by ID
@app.get("/books/{Book_id}", response_model=Book)
def get_Book(Book_id: int):
    if Book_id not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")
    return books_db[Book_id]

# POST query for creating an order
@app.post("/orders/", response_model=Order)
def create_order(order: Order):
    orders_db[order.id] = order
    return order

# GET query for retrieving an order by ID
@app.get("/orders/{order_id}", response_model=Order)
def get_order(order_id: int):
    if order_id not in orders_db:
        raise HTTPException(status_code=404, detail="Order not found")
    return orders_db[order_id]

@app.post("/customer/", response_model=User)
def create_user(user: User):
    customer_db[user.id] = user
    return user

@app.get("/customer/{user_id}", response_model=User)
def get_user(user_id: int):
    if user_id not in customer_db:
        raise HTTPException(status_code=404, detail="User not found")
    return customer_db[user_id]

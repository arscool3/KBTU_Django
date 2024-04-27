# FastAPI Application
# Add minimum 3 models with 1 relationalship
# add get, post queries for them
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class User(BaseModel):
    id: int
    username: str
    email: str

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

class Order(BaseModel):
    id: int
    user_id: int
    items: List[Item] = []

fake_db_users = {}
fake_db_orders = {}

@app.post("/users/", response_model=User)
def create_user(user: User):
    fake_db_users[user.id] = user
    return user

@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: int):
    if user_id not in fake_db_users:
        raise HTTPException(status_code=404, detail="User not found")
    return fake_db_users[user_id]

@app.post("/orders/", response_model=Order)
def create_order(order: Order):
    if order.user_id not in fake_db_users:
        raise HTTPException(status_code=404, detail="User not found")
    fake_db_orders[order.id] = order
    return order

@app.get("/orders/{order_id}", response_model=Order)
def read_order(order_id: int):
    if order_id not in fake_db_orders:
        raise HTTPException(status_code=404, detail="Order not found")
    return fake_db_orders[order_id]

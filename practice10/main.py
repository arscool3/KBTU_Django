from typing import List, Optional, Dict
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

app = FastAPI()
class User(BaseModel):
    id: int
    username: str

class Item(BaseModel):
    id: int
    name: str
    price: float
    owner_id: int

class Order(BaseModel):
    id: int
    items: List[Item]
    user_id: int

users_db: Dict[int, User] = {}
items_db: Dict[int, Item] = {}
orders_db: Dict[int, Order] = {}

@app.post("/users/", response_model=User)
def create_user(user: User):
    users_db[user.id] = user
    return user

@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id]

@app.post("/items/", response_model=Item)
def create_item(item: Item):
    items_db[item.id] = item
    return item

# GET query for retrieving an item by ID
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]

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
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Models
class User(BaseModel):
    id: int
    username: str
    email: str

class Item(BaseModel):
    id: int
    name: str
    description: str
    owner_id: int

class Order(BaseModel):
    id: int
    item_id: int
    quantity: int

# Dummy data
users = [
    User(id=1, username="user1", email="user1@example.com"),
    User(id=2, username="user2", email="user2@example.com"),
]

items = [
    Item(id=1, name="item1", description="Description for item1", owner_id=1),
    Item(id=2, name="item2", description="Description for item2", owner_id=1),
]

orders = [
    Order(id=1, item_id=1, quantity=2),
    Order(id=2, item_id=2, quantity=3),
]

# GET queries
@app.get("/users/", response_model=List[User])
async def get_users():
    return users

@app.get("/items/", response_model=List[Item])
async def get_items():
    return items

@app.get("/orders/", response_model=List[Order])
async def get_orders():
    return orders

# POST queries
@app.post("/users/", response_model=User)
async def create_user(user: User):
    users.append(user)
    return user

@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    items.append(item)
    return item

@app.post("/orders/", response_model=Order)
async def create_order(order: Order):
    orders.append(order)
    return order

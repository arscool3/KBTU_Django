from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()


# Models

class User(BaseModel):
    id: int
    username: str
    email: str


class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float


class Order(BaseModel):
    id: int
    user_id: int
    item_id: int
    quantity: int


# Sample data

users = []
items = []
orders = []


# Routes

@app.post("/users/", response_model=User)
def create_user(user: User):
    users.append(user)
    return user


@app.get("/users/", response_model=List[User])
def get_users():
    return users


@app.post("/items/", response_model=Item)
def create_item(item: Item):
    items.append(item)
    return item


@app.get("/items/", response_model=List[Item])
def get_items():
    return items


@app.post("/orders/", response_model=Order)
def create_order(order: Order):
    # Check if user and item exist
    user_exists = any(u.id == order.user_id for u in users)
    item_exists = any(i.id == order.item_id for i in items)
    if not user_exists or not item_exists:
        raise HTTPException(status_code=404, detail="User or Item not found")

    orders.append(order)
    return order


@app.get("/orders/", response_model=List[Order])
def get_orders():
    return orders

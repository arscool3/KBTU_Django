from fastapi import FastAPI, HTTPException, Depends
from models import *

app = FastAPI()

from fastapi import FastAPI

app = FastAPI()

users = []

items = []

orders = []


def get_user(user_id: int) -> User:
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

def get_item(item_id: int) -> Item:
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

def get_order(order_id: int) -> Order:
    for order in orders:
        if order.id == order_id:
            return order
    raise HTTPException(status_code=404, detail="Order not found")

@app.get("/users/{user_id}", response_model=User, tags=["Users"])
async def read_user(user: User = Depends(get_user)):
    return user

@app.post("/users/", response_model=User, tags=["Users"])
async def create_user(user: User):
    users.append(user)
    return user

@app.get("/items/{item_id}", response_model=Item, tags=["Items"])
async def read_item(item: Item = Depends(get_item)):
    return item

@app.post("/items/", response_model=Item, tags=["Items"])
async def create_item(item: Item):
    items.append(item)
    return item

@app.get("/orders/{order_id}", response_model=Order, tags=["Orders"])
async def read_order(order: Order = Depends(get_order)):
    return order

@app.post("/orders/", response_model=Order, tags=["Orders"])
async def create_order(order: Order):
    orders.append(order)
    return order

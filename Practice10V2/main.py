from fastapi import FastAPI, HTTPException, WebSocket
from pydantic import BaseModel
from typing import List
import asyncio
import random
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


class Order(BaseModel):
    id: int
    user_id: int
    item_id: int
    quantity: int


# Dummy data
users = [
    User(id=1, username="Dias", email="dias@example.com"),
    User(id=2, username="Dias2", email="dias2@example.com"),
    User(id=3, username="Dias3", email="dias3@example.com"),
]

items = [
    Item(id=1, name="milk", description="whire"),
    Item(id=2, name="phone", description="white"),
    Item(id=3, name="tv", description="big"),
]

orders = [
    Order(id=1, user_id=1, item_id=1, quantity=2),
    Order(id=2, user_id=2, item_id=2, quantity=3),
    Order(id=3, user_id=3, item_id=3, quantity=1),
]


# Routes
@app.get("/users/", response_model=List[User])
async def get_users():
    return users


@app.post("/users/")
async def create_user(user: User):
    users.append(user)
    return user


@app.get("/items/", response_model=List[Item])
async def get_items():
    return items


@app.post("/items/")
async def create_item(item: Item):
    items.append(item)
    return item


@app.get("/orders/", response_model=List[Order])
async def get_orders():
    return orders


@app.post("/orders/")
async def create_order(order: Order):
    orders.append(order)
    return order


@app.websocket("/orders/ws")
async def orders_websocket(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            order = random.choice(orders)
            await websocket.send_json(order.dict())
            await asyncio.sleep(1)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        await websocket.close()

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

class Item(BaseModel):
    id: int
    name: str
    description: str
    price: int

app = FastAPI()

items = []

@app.get('/items', response_model=List[Item])
def get_item():
    return items


@app.post("/items_post", response_model=Item)
def create_item(item: Item):
    items.append(item)
    return item


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    del items[item_id]
    return {"message": "Item deleted"}


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    items[item_id] = item
    return item
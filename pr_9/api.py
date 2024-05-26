from fastapi import FastAPI, HTTPException, Path
from .models import Item
from typing import List

app = FastAPI()

items = []


@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    items.append(item)
    return item


@app.get("/items/", response_model=List[Item])
async def read_items():
    return items


@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int = Path(..., title="The ID of the item to get")):
    try:
        return items[item_id]
    except IndexError:
        raise HTTPException(status_code=404, detail="Item not found")


@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
    try:
        items[item_id] = item
        return item
    except IndexError:
        raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    try:
        del items[item_id]
        return {"message": "Item deleted successfully"}
    except IndexError:
        raise HTTPException(status_code=404, detail="Item not found")

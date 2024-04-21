from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


inventory = {}


@app.post("/items/")
async def create_item(item: Item):
    if item.name in inventory:
        raise HTTPException(status_code=400, detail="Item already exists")
    inventory[item.name] = item
    return {"message": "Item created successfully"}


@app.get("/items/{name}")
async def read_item(name: str):
    if name not in inventory:
        raise HTTPException(status_code=404, detail="Item not found")
    return inventory[name]


@app.put("/items/{name}")
async def update_item(name: str, item: Item):
    if name not in inventory:
        raise HTTPException(status_code=404, detail="Item not found")
    inventory[name] = item
    return {"message": "Item updated successfully"}


@app.delete("/items/{name}")
async def delete_item(name: str):
    if name not in inventory:
        raise HTTPException(status_code=404, detail="Item not found")
    del inventory[name]
    return {"message": "Item deleted successfully"}

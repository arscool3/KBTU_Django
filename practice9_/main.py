# CREATE 3 VIEWS WITH DEPENDECY INJECTION
# 2 WITH FUNCTION DEPENDENCY INJECTION
# 1 WITH INSTANCE OF CLASS AS CALLABLE DI

from fastapi import FastAPI, Depends, HTTPException
from typing import List

app = FastAPI()

# Sample data
inventory = {
    'apples': 10,
    'bananas': 20,
    'oranges': 15
}


class Inventory:
    def __init__(self):
        self.inventory = inventory

    def check_item_availability(self, item_name: str):
        if item_name in self.inventory:
            return True
        else:
            return False

inventory_instance = Inventory()

# Dependency
def get_inventory():
    return inventory_instance


# Views
@app.get("/")
async def read_root():
    return {"message": "Welcome to the grocery store!"}


@app.get("/items/{item_name}")
async def read_item(item_name: str, inventory: Inventory = Depends(get_inventory)):
    if inventory.check_item_availability(item_name):
        return {"item_name": item_name, "available": True}
    else:
        return {"item_name": item_name, "available": False}


# Function with Dependency Injection
@app.get("/list_items/")
async def list_items(inventory: Inventory = Depends(get_inventory)):
    return {"items_available": inventory.inventory}


@app.get("/count_items/")
async def count_items(inventory: Inventory = Depends(get_inventory)):
    total_items = sum(inventory.inventory.values())
    return {"total_items": total_items}
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello:app")
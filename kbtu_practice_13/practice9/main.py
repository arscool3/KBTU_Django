from typing import Dict, List
import logging
from fastapi import FastAPI, HTTPException, Depends, Response, Header
from pydantic import BaseModel

from nodels import Product
from logger import get_logger
from auth import check_api_key

app = FastAPI()


product_data = [
    {"name": "apple", "price": 10.0, "amount": 100},
    {"name": "banana", "price": 5.0, "amount": 50},
    {"name": "orange", "price": 8.0, "amount": 75}
]
database: List[Product] = [Product(**item) for item in product_data]

def get_database():
    return database


class ProductManager:
    def __init__(self, database: List[Product]):
        self.database = database

    def add_product(self, product: Product):
        if product in self.database:
            raise HTTPException(status_code=400, detail="Product already exists")
        self.database.append(product)
        return {"message": f"Product '{product.name}' added successfully"}

    def buy_product(self, name: str, amount: int):
        product = next((p for p in self.database if p.name == name), None)
        if product is None:
            raise HTTPException(status_code=404, detail="Product not found")
        if product.amount - amount < 0:
            raise HTTPException(status_code=400, detail="Product out of stock")
        product.amount -= amount
        return {"message": f"Bought {amount} '{name}' for {product.price * amount}. Remaining stock: {product.amount}"}

    def get_product_price(self, name: str):
        product = next((p for p in self.database if p.name == name), None)
        if product is None:
            raise HTTPException(status_code=404, detail="Product not found")
        return {"price": product.price, "name": name}


def get_product_manager(database: List[Product] = Depends(get_database)):
    return ProductManager(database)


product_manager = get_product_manager(database)

# Endpoints
@app.post("/products/", response_model=dict)
async def add_product(product: Product, logger=Depends(get_logger)):
    logger.info(f"Adding product: {product}")
    result = product_manager.add_product(product)
    return result


@app.post("/buy/{name}/{amount}", response_model=dict, dependencies=[Depends(check_api_key)])
async def buy_product(name: str, amount: int, logger=Depends(get_logger)):
    logger.info(f"Buying product: {name}, amount: {amount}")
    result = product_manager.buy_product(name, amount)
    return result

@app.get("/price/{name}", response_model=dict)
async def get_product_price(name: str, logger=Depends(get_logger)):
    logger.info(f"Getting price for product: {name}")
    result = product_manager.get_product_price(name)
    return result

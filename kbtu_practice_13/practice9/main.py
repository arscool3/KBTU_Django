from typing import Dict

import logging
from fastapi import FastAPI, HTTPException, Depends, Response

from .nodels import Product
from .logger import get_logger
from .auth import check_api_key
app = FastAPI()

# Database Dependency
original_database = {
    "apple": Product(name="apple", price=10.0, amount=100),
    "banana": Product(name="banana", price=5.0, amount=50),
    "orange": Product(name="orange", price=8.0, amount=75)
}


def get_database():
    return original_database


def get_product_manager(database: Dict = Depends(get_database)):
    return ProductManager(database)


class ProductManager:
    def __init__(self, database: Dict):
        self.database = database

    def add_product(self, product: Product):
        if product.name in self.database:
            raise HTTPException(status_code=400, detail="Product already exists")
        self.database[product.name] = product
        return {"message": f"Product '{product.name}' added successfully"}

    def buy_product(self, name: str, amount: int):
        if name not in self.database:
            raise HTTPException(status_code=404, detail="Product not found")
        product = self.database[name]
        if product.amount - amount < 0:
            raise HTTPException(status_code=400, detail="Product out of stock")
        product.amount -= amount
        return {"message": f" {amount} '{name}' bought successfully. Remains: {product.amount}"}

    def get_product_price(self, name: str):
        if name not in self.database:
            raise HTTPException(status_code=404, detail="Product not found")
        return {"price": self.database[name].price, "name": name}


product_manager = get_product_manager()


@app.post("/products/")
async def add_product(product: Product, product_manager: ProductManager = Depends(), logger=Depends(get_logger())):
    logger.info(f"Adding product: {product}")
    result = product_manager.add_product(product)
    return Response(content=result, status_code=200)


@app.post("/buy/{name}/{amount}")
async def buy_product(name: str, amount: int,
                      product_manager: ProductManager = Depends(),
                      logger=Depends(get_logger),
                      auth: None = Depends(check_api_key)):
    logger.info(f"Buying product: {name}, amount: {amount}")
    result = product_manager.buy_product(name, amount)
    return Response(content=result, status_code=200)


@app.get("/price/{name}")
async def get_product_price(name: str, product_manager: ProductManager = Depends(), logger=Depends(get_logger())):
    logger.info(f"Watching price: {name}")
    result = product_manager.get_product_price(name)
    return Response(content=result, status_code=200)

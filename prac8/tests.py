from datetime import datetime
from fastapi import FastAPI
import pydantic

app = FastAPI()

shops = []
products = []


class Product(pydantic.BaseModel):
    id: int = pydantic.Field()
    name: str = pydantic.Field(max_length=30)
    price: float = pydantic.Field()


class Shop(pydantic.BaseModel):
    name: str = pydantic.Field(max_length=40)
    city: str = pydantic.Field(max_length=30)
    address: str = pydantic.Field(max_length=50)
    products: Product


@app.get("/products")
def get_prods():
    return products


@app.post("/add_shop")
def add_shop(shop: Shop) -> list[Shop]:
    shops.append(shop)
    return shops


@app.post("/add_product")
def add_product(product: Product):
    products.append(product)
    return products


@app.delete("/del_product")
def del_product(id: int):
    products.pop(id)
    return products


@app.put("/upd_product/{prod_id}")
def upd_product(prod_id: int, product: Product):
    products[prod_id] = product
    return {"message": "Product updated successfully", "product": product}
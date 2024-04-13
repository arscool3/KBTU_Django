from datetime import datetime
from fastapi import FastAPI
import pydantic

app = FastAPI()

shops = []
products = []


class Product(pydantic.BaseModel):
    name: str = pydantic.Field(max_length=30)
    price: float = pydantic.Field()


class Shop(pydantic.BaseModel):
    name: str = pydantic.Field(max_length=40)
    city: str = pydantic.Field(max_length=30)
    address: str = pydantic.Field(max_length=50)
    products: Product


@app.get("/")
def test(num: int):
    return num

@app.post("/add_shop")
def add_shop(shop: Shop) -> list[Shop]:
    shops.append(shop)
    return shops

@app.post("/add_product")
def add_product(product: Product):
    products.append(product)
    return products

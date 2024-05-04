# pip install fastapi uvicorn pydantic
from datetime import datetime
from fastapi import FastAPI
from enum import StrEnum
import pydantic

app = FastAPI()


class Meat(StrEnum):
    beef = "beef"
    chicken = "chicken"
    assorti = "assorti"


class Donerka(StrEnum):
    kbtu = "kbtu"
    marmaris = "marmaris"
    big_doner = "big_doner"
    kervan_doner = "kervan_doner"


class Pizza(pydantic.BaseModel):
    sauce: str = pydantic.Field(max_length=10)
    size: int = pydantic.Field(gt=5)
    model_config = pydantic.ConfigDict(frozen=True)


class Doner(pydantic.BaseModel):
    meat: Meat
    donerka: Donerka
    price: int = pydantic.Field(description='price for doner', lt=10_000)


class Order(pydantic.BaseModel):
    pizzas: list[Pizza]
    doners: list[Doner]
    created_at: datetime = datetime.now()


orders = []


@app.get("/")
def test(param_pam_pam: int) -> dict:
    return {'your_param': param_pam_pam}


@app.post("/")
def add_order(order: Order) -> list[Order]:
    orders.append(order)
    return orders





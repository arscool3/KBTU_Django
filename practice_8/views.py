from fastapi import FastAPI
from enum import StrEnum
import pydantic
from datetime import datetime
app = FastAPI()


class Painting(StrEnum):
    oil= "oily"
    acryl ="acryl"
    gouache= "gouache"
    watercolor= "watercolor"


class Painting_studio(StrEnum):
    studiofes= "studiofes"
    art_club = "art_club"
    ametures= "ametures"
    real_artists="realart"


class Photo(pydantic.BaseModel):
    length: int = pydantic.Field(gt=5)
    width: int = pydantic.Field(gt=5)
    model_config = pydantic.ConfigDict(frozen=True)


class Picture(pydantic.BaseModel):
    painting: Painting
    painting_studio: Painting_studio
    price: int = pydantic.Field(description='price for Picture', lt=10_000)


class Order(pydantic.BaseModel):
    photos: list[Photo]
    pictures: list[Picture]
    created_at: datetime = datetime.now()


orders = []


@app.get("/")
def test(param_pam_pam: int) -> dict:
    return {'your_param': param_pam_pam}


@app.post("/")
def add_order(order: Order) -> list[Order]:
    orders.append(order)
    return orders



@app.put("/")
def update_order(order_id: int, new_order: Order) -> Order:
    if order_id < len(orders):
        orders[order_id] = new_order
        return new_order
    else:
        return {"error": "Order ID not found"}


@app.delete("/")
def delete_order(order_id: int) -> dict:
    if order_id < len(orders):
        deleted_order = orders.pop(order_id)
        return {"deleted_order": deleted_order}
    else:
        return {"error": "Order ID not found"}
from typing import List

from fastapi import FastAPI
import pydantic

app = FastAPI()

class Product(pydantic.BaseModel):
    id: int = pydantic.Field(ge=0)
    name: str = pydantic.Field(max_length=255)
    cost: int = pydantic.Field(ge=0)

    def getid(self):
        return self.id
    def change(self, name: str, cost: int):
        self.name = name
        self.cost = cost

Products = []

@app.get("/products")
def show_products():
    return {"status": 200, "data": Products}


@app.get("/products/{pr_id}", response_model=List[Product])
def show_product(pr_id: int):
    return [p for p in Products if p.getid() == pr_id]

@app.post("/product")
def add_product(prds: Product):
    Products.append(prds)
    return {"status": 200, "data": Products}


@app.delete("/products/{pr_id}", response_model=List[Product])
def delete_product(pr_id: int):
    for i in range(len(Products)):
        if Products[i].getid() == pr_id:
            Products.pop(i)
    return Products

@app.put("/products/{pr_id}")
def edit_product(pr_id: int, name: str, cost: int):
    for i in range(len(Products)):
        if Products[i].getid() == pr_id:
            Products[i].change(name, cost)

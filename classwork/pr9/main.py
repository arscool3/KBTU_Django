from typing import List, Annotated

from fastapi import FastAPI, Depends
import pydantic

app = FastAPI()

my_id = ''

class Product(pydantic.BaseModel):
    id: int = pydantic.Field(ge=0)
    name: str = pydantic.Field(max_length=255)
    cost: int = pydantic.Field(ge=0)

    def getid(self):
        return self.id

    def getname(self):
        return self.name

    def getcost(self):
        return self.cost

    def change(self, name: str, cost: int):
        self.name = name
        self.cost = cost


Products = []


# Dependency injection expl 1

def FindProduct(id: int) -> int:
    for i in range(len(Products)):
        if Products[i].getid() == id:
            return i

# Dependency 2
def Search(s: str):
    Prs = []
    for i in range(len(Products)):
        if s in Products[i].getname():
            Prs.append(Products[i])
    return Prs

# Dependency 3
def biger(cost: int):
    Prs = []
    for i in range(len(Products)):
        if Products[i].getcost() > cost:
            Prs.append(Products[i])
    return Prs

# Product
@app.get("/products")
def show_products():
    return {"status": 200, "data": Products}

@app.get("/products/show/{pr_id}", response_model=List[Product])
def show_product(pr_id: int):
    return [p for p in Products if p.getid() == pr_id]

@app.get("/products/search", response_model=List[Product])
def searchProducts(key: Annotated[str, Depends(Search)]):
    return key

@app.get("/products/morethan", response_model=List[Product])
def ProductsMore(cost: Annotated[int, Depends(biger)]):
    return cost

@app.post("/product")
def add_product(prds: Product):
    Products.append(prds)
    return {"status": 200, "data": Products}

@app.delete("/products/{pr_id}", response_model=List[Product])
def delete_product(pr_id: Annotated[int, Depends(FindProduct)]):
    Products.pop(pr_id)
    return Products

@app.put("/products/{pr_id}", response_model=List[Product])
def edit_product(pr_id: Annotated[int, Depends(FindProduct)], name: str, cost: int):
    Products[pr_id].change(name, cost)
    return Products




from fastapi import FastAPI, Depends
from sqlalchemy import select, insert
import schemas as sch
import database as db
import models as mdl
from fastapi import HTTPException
from sqlalchemy.orm import Session
from database import session
from repository import *

app = FastAPI()



def get_db():
    try:
        yield session
        session.commit()
    except:
        raise
    finally:
        session.close()

def get_product_repo(db: Session = Depends(get_db)):
    return ProductRepository(db)

def get_category_repo(db: Session = Depends(get_db)):
    return CategoryRepository(db)


@app.post("/products")
def add_product(product: sch.Product, service: ProductRepository = Depends(get_product_repo)):
    service.create_product(product)

@app.get("/products/{category_id}")
def get_product_by_category(category_id: int, service: ProductRepository = Depends(get_product_repo)):
    service.get_products_by_category(category_id)

@app.post("/categories/add")
def add_category(category: sch.Category, service: CategoryRepository = Depends(get_category_repo)):
    service.create_category(category)

@app.get("/categories")
def get_product_by_category(service: CategoryRepository = Depends(get_category_repo)):
    service.get_categories()
    

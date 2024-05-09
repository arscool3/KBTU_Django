from fastapi import FastAPI, Depends
from sqlalchemy import select, insert
import schemas as sch
import models as mdl
from fastapi import HTTPException
from sqlalchemy.orm import Session

class ProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_product(self, product: sch.Product):
        self.db.add(mdl.Product(**product.model_dump()))
        return "Products was added"
    
    def get_products_by_category(self, id: int):
        db_products = self.db.query(mdl.Product).filter(
                        mdl.Product.category_id == id
                        ).all()
        return [sch.Product.model_validate(product) for product in db_products]

class CategoryRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_category(self, category: sch.Category):
        self.db.add(mdl.Category(**category.model_dump()))
        return "Category was added"
    
    def get_categories(self):
        db_categories = self.db.query(mdl.Category).all()
        return [sch.Category.model_validate(category) for category in db_categories]


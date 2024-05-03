from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Create FastAPI app instance
app = FastAPI()

# SQLAlchemy database connection
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Models
class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    products = relationship("Product", back_populates="category")

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Integer)
    category_id = Column(Integer, ForeignKey("categories.id"))

    category = relationship("Category", back_populates="products")

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

# Create tables in the database
Base.metadata.create_all(bind=engine)

# API routes
@app.post("/categories/")
def create_category(name: str):
    db = SessionLocal()
    category = Category(name=name)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category

@app.get("/categories/{category_id}/")
def get_category(category_id: int):
    db = SessionLocal()
    category = db.query(Category).filter(Category.id == category_id).first()
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@app.post("/products/")
def create_product(name: str, price: int, category_id: int):
    db = SessionLocal()
    product = Product(name=name, price=price, category_id=category_id)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

@app.get("/products/{product_id}/")
def get_product(product_id: int):
    db = SessionLocal()
    product = db.query(Product).filter(Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.post("/customers/")
def create_customer(name: str):
    db = SessionLocal()
    customer = Customer(name=name)
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer

@app.get("/customers/{customer_id}/")
def get_customer(customer_id: int):
    db = SessionLocal()
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

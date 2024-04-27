from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, Session
from typing import List, Optional

DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost/postgres"

Base = declarative_base()

# Models
class User(Base):
  __tablename__ = "users"

  id = Column(Integer, primary_key=True, index=True)
  username = Column(String, unique=True, index=True)
  email = Column(String, unique=True, index=True)

  items = relationship("Item", back_populates="owner")


class Item(Base):
  __tablename__ = "items"

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, index=True)
  description = Column(String)
  owner_id = Column(Integer, ForeignKey("users.id"))

  owner = relationship("User", back_populates="items")


class Order(Base):
  __tablename__ = "orders"

  id = Column(Integer, primary_key=True, index=True)
  user_id = Column(Integer, ForeignKey("users.id"))
  item_id = Column(Integer, ForeignKey("items.id"))
  quantity = Column(Integer)

# Engine and session
engine = create_engine(DATABASE_URL, echo=True, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()

# Dependency to get DB session
def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

# POST endpoints
@app.post("/users/", response_model=User)
async def create_user(user: User, db: Session = Depends(get_db)):
  db.add(user)
  db.commit()
  db.refresh(user)
  return user

@app.post("/items/", response_model=Item)
async def create_item(item: Item, db: Session = Depends(get_db)):
  db.add(item)
  db.commit()
  db.refresh(item)
  return item

@app.post("/orders/", response_model=Order)
async def create_order(order: Order, db: Session = Depends(get_db)):
  db.add(order)
  db.commit()
  db.refresh(order)

  return order

# GET endpoints
@app.get("/users/", response_model=List[User])
async def get_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
  return db.query(User).offset(skip).limit(limit).all()

@app.get("/items/", response_model=List[Item])
async def get_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
  return db.query(Item).offset(skip).limit(limit).all()

@app.get("/orders/", response_model=List[Order])
async def get_orders(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
  return db.query(Order).offset(skip).limit(limit).all()

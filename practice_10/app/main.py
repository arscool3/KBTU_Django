from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Create a SQLite database in memory
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# Create SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Create a SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declare a base class for SQLAlchemy models
Base = declarative_base()

# Define the models
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    items = relationship("Item", back_populates="owner")

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")

# Create all tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# Pydantic models for request and response
class UserIn(BaseModel):
    name: str
    email: str

class UserOut(BaseModel):
    id: int
    name: str
    email: str

class ItemIn(BaseModel):
    title: str
    description: str

class ItemOut(BaseModel):
    id: int
    title: str
    description: str
    owner: UserOut

# Routes
@app.post("/users/", response_model=UserOut)
def create_user(user: UserIn):
    db = SessionLocal()
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        existing_user.name = user.name
        db.commit()
        db.refresh(existing_user)
        db.close()
        return {
            "id": existing_user.id,
            "name": existing_user.name,
            "email": existing_user.email
        }
    new_user = User(name=user.name, email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    db.close()
    return {
        "id": new_user.id,
        "name": new_user.name,
        "email": new_user.email
    }


@app.get("/users/{user_id}", response_model=UserOut)
def read_user(user_id: int):
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.close()
    return user

@app.post("/items/", response_model=ItemOut)
def create_item(item: ItemIn, user_id: int):
    db = SessionLocal()
    owner = db.query(User).filter(User.id == user_id).first()
    if owner is None:
        raise HTTPException(status_code=404, detail="User not found")
    new_item = Item(title=item.title, description=item.description, owner_id=user_id)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    db.close()
    return new_item

@app.get("/items/{item_id}", response_model=ItemOut)
def read_item(item_id: int):
    db = SessionLocal()
    item = db.query(Item).filter(Item.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.close()
    return item


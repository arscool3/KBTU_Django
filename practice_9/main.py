from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Dependency 1
def get_db():
    db = {"name": "test_db"}
    return db

# Dependency 2
def get_user(db: dict = Depends(get_db)):
    user = db.get("user")
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Dependency 3
def get_book(db: dict = Depends(get_db)):
    book = db.get("book")
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


class User(BaseModel):
    name: str

class Book(BaseModel):
    title: str
    author: str

@app.get("/user", response_model=User)
async def get_user(user: User = Depends(get_user)):
    return user

@app.get("/book", response_model=Book)
async def get_book(book: Book = Depends(get_book)):
    return book

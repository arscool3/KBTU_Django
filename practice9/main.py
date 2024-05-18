from fastapi import Depends, FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()
database = "Fake Database"

def get_db():
    return database

@app.get("/")
def read_root(db: str = Depends(get_db)):
    return {"message": f"Connected to {db}"}

class Database:
    def __init__(self):
        self.db = "Fake Database"

    def get_db(self):
        return self.db

db_instance = Database()

@app.get("/db")
def read_db(db: str = Depends(db_instance.get_db)):
    return {"message": f"Connected to {db}"}

def create_database():
    return "Fake Database"

@app.get("/create_db")
def read_create_db(db: str = Depends(create_database)):
    return {"message": f"Connected to {db}"}

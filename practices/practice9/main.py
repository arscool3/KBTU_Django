from fastapi import FastAPI, Depends, HTTPException
from typing import Optional

app = FastAPI()


# Example 1: Dependency as a function
def get_token():
    return "fake-token"


@app.get("/")
def read_root(token: str = Depends(get_token)):
    return {"token": token}


# Example 2: Dependency as a class
class FakeDB:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_items(self):
        return self.items


fake_db = FakeDB()


@app.post("/items/")
def create_item(item: str, db: FakeDB = Depends()):
    db.add_item(item)
    return {"item": item}


@app.get("/items/")
def read_items(db: FakeDB = Depends()):
    return {"items": db.get_items()}


# Example 3: Dependency with optional parameters
def get_query(q: Optional[str] = None):
    return q


@app.get("/query/")
def read_query(query: str = Depends(get_query)):
    if query is None:
        return {"query": "No query provided"}
    return {"query": query}

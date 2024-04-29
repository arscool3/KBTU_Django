from typing import List, Type

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users = []


class User(BaseModel):
    id: int
    name: str


@app.get("/")
async def read_root():
    return {"message": "Hello, World"}


@app.get("/users")
async def read_users():
    return users


@app.post("/users")
async def create_user(user:  User):
    users.append(user)
    return {"message": "Successfully created user"}


@app.put("/users/{user_id}")
async def update_user(user_id: int, user: User):
    for u in users:
        if u.id == user_id:
            u.id = user.id
            u.name = user.name

    return {"message": "Successfully updated"}


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    for u in users:
        if u.id == user_id:
            users.remove(u)

    return {"message": "Successfully deleted"}

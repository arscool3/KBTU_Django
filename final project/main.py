from entity import User
from fastapi import FastAPI

app = FastAPI()

users = [ User(username='Tolganai'),
         User(username='Asel'
            
         )]

@app.get("/user")
def users() -> list[User]:
    return users

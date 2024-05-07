from fastapi import FastAPI, Depends, HTTPException, Header
from pydantic import BaseModel

app = FastAPI()

# Example 1: Dependency Injection using Parameters
async def get_token_header(x_token: str = Header(None)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")
    return x_token

@app.get("/items/")
async def read_items(token: str = Depends(get_token_header)):
    return {"token": token}


# Example 2: Dependency Injection using Functions
def fake_decode_token(token):
    return {"fake_user_id": "123", "fake_user_name": "fake_user"}

async def get_query_token(token: str):
    return fake_decode_token(token)

@app.get("/users/")
async def read_users(token_data: dict = Depends(get_query_token)):
    return {"token_data": token_data}


# Example 3: Dependency Injection using Classes
class FakeUser:
    def __init__(self, username: str, id: str):
        self.username = username
        self.id = id

async def get_fake_user(token_data: dict = Depends(get_query_token)):
    user = FakeUser(username=token_data['fake_user_name'], id=token_data['fake_user_id'])
    return user

@app.get("/fake_users/")
async def read_fake_users(fake_user: FakeUser = Depends(get_fake_user)):
    return {"fake_user": fake_user.__dict__}
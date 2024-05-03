from fastapi import FastAPI
from pydantic import BaseModel, UUID4
from typing import List, Optional
import uuid
from datetime import datetime

app = FastAPI()

# Define Pydantic models for FastAPI
class ClientBase(BaseModel):
    name: str
    surname: str
    email: Optional[str] = None
    phone: Optional[str] = None

class ClientCreate(ClientBase):
    pass

class Client(ClientBase):
    id: UUID4

    class Config:
        orm_mode = True

class ManagerBase(BaseModel):
    name: str

class ManagerCreate(ManagerBase):
    pass

class Manager(ManagerBase):
    id: UUID4

    class Config:
        orm_mode = True

class RequestBase(BaseModel):
    client_id: UUID4
    manager_id: UUID4
    title: str
    description: str

class RequestCreate(RequestBase):
    pass

class Request(RequestBase):
    id: UUID4
    created_at: Optional[str]

    class Config:
        orm_mode = True


db = {"clients": [], "managers": [], "requests": []}

@app.post("/clients/", response_model=Client)
async def create_client(client: ClientCreate):
    data = client.dict()
    data["id"] = uuid.uuid4()
    db["clients"].append(data)
    return data

@app.get("/clients/", response_model=List[Client])
async def read_clients():
    return db["clients"]

@app.post("/managers/", response_model=Manager)
async def create_manager(manager: ManagerCreate):
    data = manager.dict()
    data["id"] = uuid.uuid4()
    db["managers"].append(data)
    return data

@app.get("/managers/", response_model=List[Manager])
async def read_managers():
    return db["managers"]

@app.post("/requests/", response_model=Request)
async def create_request(request: RequestCreate):
    data = request.dict()
    data["id"] = uuid.uuid4()
    data["created_at"] = datetime.now()
    db["requests"].append(data)
    return data

@app.get("/requests/", response_model=List[Request])
async def read_requests():
    return db["requests"]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
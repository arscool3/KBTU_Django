from typing import List, Optional
from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str
    email: str

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

class Order(BaseModel):
    id: int
    user_id: int
    items: List[Item]


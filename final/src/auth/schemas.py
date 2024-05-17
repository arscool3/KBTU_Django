from enum import Enum
from pydantic import BaseModel
from typing import Union

class RoleEnum(str, Enum):
    STUDENT = "STUDENT"
    INSTRUCTOR = "INSTRUCTOR"

class UserBase(BaseModel):
    username: str
    email: str
    password: str
    role: RoleEnum

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Union[str, None] = None
    scopes: list[str] = []

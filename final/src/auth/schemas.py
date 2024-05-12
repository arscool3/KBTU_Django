from enum import Enum
from pydantic import BaseModel
from typing import Union

class RoleEnum(str, Enum):
    STUDENT = "STUDENT"
    INSTRUCTOR = "INSTRUCTOR"

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    role: RoleEnum

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Union[str, None] = None

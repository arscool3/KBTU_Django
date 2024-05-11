from enum import Enum
from pydantic import BaseModel

class RoleEnum(str, Enum):
    STUDENT = "STUDENT"
    INSTRUCTOR = "INSTRUCTOR"

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    role: RoleEnum

from pydantic import BaseModel

class User(BaseModel):
    username: str
    class Config:
       from_attributes = True
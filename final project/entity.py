from pydantic import BaseModel

class User(BaseModel):
    id:int
    username: str
    class Config:
       from_attributes = True
class Recipe(BaseModel):
    id:int
    title: str
    description: str
    class Config:
       from_attributes = True

class Article(BaseModel):
    id: int
    
    title: str
    description: str
    class Config:
       from_attributes = True

class Ingredient(BaseModel):
    id: int
    title: str
    description: str
    class Config:
       from_attributes = True
from pydantic import BaseModel
from typing import List, Optional

class Ingredient(BaseModel):
   
    title: str
    description: str
    class Config:
        from_attributes  = True

class Comment(BaseModel):
    
    title: str
    description: str
    class Config:
        from_attributes  = True

class Recipe(BaseModel):

    title: str
    description: str
    comments: List[Comment]
    ingredients: List[Ingredient]
    class Config:
        from_attributes  = True

class Category(BaseModel):

    title: str
    description: str
    class Config:
        from_attributes  = True

class Article(BaseModel):
   
    title: str
    description: str
    class Config:
        from_attributes  = True

class User(BaseModel):
   
    username: str
    recipes: Optional[List[Recipe]] = []
    articles: Optional[List[Article]] = []
    class Config:
        from_attributes  = True
from pydantic import BaseModel
from typing import List, Optional

class Ingredient(BaseModel):
    id: int
    description: str
    class Config:
        from_attributes  = True

class Comment(BaseModel):
    id: int
    description: str
    class Config:
        from_attributes  = True

class Recipe(BaseModel):
    id: int
    user_id: int
    title: str
    description: str
    comments: List[Comment]
    ingredients: List[Ingredient]
    class Config:
        from_attributes  = True

class Category(BaseModel):
    id: int
    title: str
    class Config:
        from_attributes  = True

class Article(BaseModel):
    id: int
    user_id: int
    title: str
    description: str
    class Config:
        from_attributes  = True

class User(BaseModel):
    id: int
    username: str
    recipes: List[Recipe]
    articles: List[Article]
    class Config:
        from_attributes  = True
from pydantic import BaseModel
from typing import List, Optional

class Comment(BaseModel):
    id: int
    title: str
    description: str
    article_id: int

    class Config:
        orm_mode = True

class Recipe(BaseModel):
    id: int
    title: str
    description: str
    user_id: int
    ingredients: Optional[List['Ingredient']] = []
    categories: Optional[List['Category']] = []

    class Config:
        orm_mode = True

class Category(BaseModel):
    id: int
    title: str
    description: str
    recipes: Optional[List[Recipe]] = []

    class Config:
        orm_mode = True

class Article(BaseModel):
    id: int
    title: str
    description: str
    user_id: int
    comments: Optional[List[Comment]] = []

    class Config:
        orm_mode = True

class Ingredient(BaseModel):
    id: int
    title: str
    description: str
    recipes: Optional[List[Recipe]] = []

    class Config:
        orm_mode = True

class User(BaseModel):
    id: int
    username: str
    recipes: Optional[List[Recipe]] = []
    articles: Optional[List[Article]] = []

    class Config:
        orm_mode = True

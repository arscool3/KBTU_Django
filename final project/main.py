from fastapi import FastAPI, HTTPException
from typing import List
from entity import Recipe, User

app = FastAPI()

# Mock data for demonstration
users = [
    User(id=1, username="user1"),
    User(id=2, username="user2"),
]

recipes = [
    Recipe(id=1, user_id=1, title="Recipe 1", description="Description 1", comments=[], ingredients=[]),
    Recipe(id=2, user_id=2, title="Recipe 2", description="Description 2", comments=[], ingredients=[]),
]

@app.get("/recipes", response_model=List[Recipe])
def get_recipes():
    return recipes

@app.get("/users/{user_id}/recipes", response_model=List[Recipe])
def get_user_recipes(user_id: int):
    user_recipes = [recipe for recipe in recipes if recipe.user_id == user_id]
    if not user_recipes:
        raise HTTPException(status_code=404, detail="User not found")
    return user_recipes

from fastapi import FastAPI
from contextlib import contextmanager
from typing import Optional, Annotated

from sqlalchemy import select
from models import Recipe
from fastapi import FastAPI, HTTPException, Depends
import models as db
app = FastAPI()

@app.get("/")
def test():
    return("ok")

@contextmanager
def get_db():
    try:
        session = db.session
        yield session
        session.commit()
        session.close()
    except Exception:
        print('some exception')


@app.get("/recipe")
def recipe(id: int) -> db.Recipe:
    with get_db() as session:
        recipe = session.get(db.Recipe, id)
        if recipe is None:
            raise HTTPException(status_code=404)
        return db.Recipe.model_validate(recipe)


@app.get("/recipes")
def recipes() -> list[Recipe]:
    with get_db() as session:
        db_recipes = session.execute(select(db.Recipe)).scalars().all()
        recipes = []
        for db_car in db_recipes:
            recipes.append(Recipe.model_validate(db_car))
        return recipes

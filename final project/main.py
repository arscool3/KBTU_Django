from fastapi import FastAPI, HTTPException, Depends
from contextlib import contextmanager
from sqlalchemy import select
from entity import Ingredient, Recipe, Article
import models as db

app = FastAPI()


@contextmanager
def get_db():
    try:
        session = db.session
        yield session
        session.commit()
        session.close()
    except Exception:
        print('Some exception')


@app.get("/ingredient")
def ingredient(id: int) -> Ingredient:
    with get_db() as session:
        ingredient = session.get(db.Ingredient, id)
        if ingredient is None:
            raise HTTPException(status_code=404)
        return Ingredient.model_validate(ingredient)





class AddDependency:

    @staticmethod
    def _add_model(db_model: type[db.Ingredient] | type[db.Recipe] | type[db.Article], pydantic_model: Ingredient | Recipe | Article) -> None:
        with get_db() as session:
            session.add(db_model(**pydantic_model.model_dump()))

    @classmethod
    def add_ingredient(cls, ingredient: Ingredient) -> str:
        cls._add_model(db.Ingredient, ingredient)
        return "Ingredient was added"

    @classmethod
    def add_recipe(cls, recipe: Recipe) -> str:
        cls._add_model(db.Recipe, recipe)
        return "Recipe was added"

    @classmethod
    def add_article(cls, article: Article) -> str:
        cls._add_model(db.Article, article)
        return "Article was added"


@app.post("/ingredient")
def add_ingredient(ingredient_di: str = Depends(AddDependency.add_ingredient)) -> str:
    return ingredient_di


@app.post("/recipe")
def add_recipe(recipe_di: str = Depends(AddDependency.add_recipe)) -> str:
    return recipe_di


@app.post("/article")
def add_article(article_di: str = Depends(AddDependency.add_article)) -> str:
    return article_di

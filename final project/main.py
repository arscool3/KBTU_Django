from http import HTTPStatus
from fastapi import FastAPI, HTTPException, Depends, Request
from contextlib import contextmanager
from sqlalchemy import select
from entity import Ingredient, Recipe, Article
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.orm import Session
from models import User,  get_user_by_username, verify_password
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import models as db
from dramatiq.results.errors import ResultMissing
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import secrets, uvicorn

from tasks import add_employee_task, result_backend

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

@app.get("/ingredient_availability")
def get_response(message_id: str):
    try:
        status = result_backend.get_result(add_employee_task.message().copy(message_id=message_id))
    except ResultMissing:
        return {"status": "pending"}
    return {'status': status + " the ingredient is raised in your current area and available in this season "}

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


security = HTTPBasic()
templates = Jinja2Templates(directory="templates")

def authenticate_user(credentials: HTTPBasicCredentials = Depends(security)):
    user = db.get(credentials.username)
    if not user or not secrets.compare_digest(user["password"], credentials.password):
        raise HTTPException(
            status_code=HTTPStatus.HTTP_401_UNAUTHORIZED,  
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/protected")
def read_protected(username: str = Depends(authenticate_user)):
    return {"message": f"Hello {username}, you are authenticated"}

@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

if __name__ == "__main__":
    
    uvicorn.run(app, host="0.0.0.0", port=8000)
from fastapi import FastAPI
import models
import database
from auth import router as auth_router

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(auth_router.router)

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}


# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}
# from typing import Annotated

# from fastapi import Depends, FastAPI
# from fastapi.security import OAuth2PasswordBearer


# app = FastAPI()


# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


# @app.get("/items/")
# async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
#     return {"token": token}
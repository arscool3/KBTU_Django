from fastapi import FastAPI

from db import engine
import models
import users
import comments
import posts

api = FastAPI()

models.Base.metadata.create_all(bind=engine)


api.include_router(users.router)
api.include_router(posts.router)
api.include_router(comments.router)
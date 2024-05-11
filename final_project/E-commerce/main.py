from fastapi import FastAPI
from database import models
from database.db import engine
from api import api


app = FastAPI()
app.include_router(api.router)

models.Base.metadata.create_all(bind=engine)

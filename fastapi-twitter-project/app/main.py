from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
from .models import *
from . import models
from .database import engine


from .routers import tweet, users, auth, like

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tweet.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(like.router)


@app.get("/")
async def root():
    return {"message": "Hello World!"}
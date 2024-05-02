from fastapi import FastAPI
from database import engine, Base
from routers import users, posts, comments

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(posts.router)
app.include_router(comments.router)

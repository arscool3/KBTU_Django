# main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise

from .routers import seed_router

app = FastAPI()

# Allowing CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registering the seed router
app.include_router(seed_router.router)

# Registering Tortoise ORM with FastAPI
register_tortoise(
    app,
    db_url="postgres://user:password@localhost:5432/seeds",
    modules={"models": ["app.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

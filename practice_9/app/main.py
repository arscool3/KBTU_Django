from fastapi import FastAPI
from .routes import items, users, config
from .dependencies import database, users as user_deps, config as config_deps

app = FastAPI()

app.include_router(items.router)
app.include_router(users.router)
app.include_router(config.router)

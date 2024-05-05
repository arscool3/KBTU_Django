from fastapi import FastAPI
from .routers import user_router, post_router, comment_router
from database import engine, Base
from .websockets import websocket_router


app = FastAPI()

# Include routers
app.include_router(user_router)
app.include_router(post_router)
app.include_router(comment_router)
app.include_router(websocket_router)

# Initialize database tables
init_db()
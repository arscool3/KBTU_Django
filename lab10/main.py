from fastapi import FastAPI
from .routers import user_router, post_router, comment_router
from database import engine, Base

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(user_router)
app.include_router(post_router)
app.include_router(comment_router)

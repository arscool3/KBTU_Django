from fastapi import FastAPI
from database.database import engine,Base
from models.models import User, Event, Venue, Category, Booking, Location
from routes.routes import create_user, read_user, update_user, delete_user
# Create tables in the database
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# Include routers and endpoints for your application
# Example: from .routers import user, event, etc.
app.include_router(create_user)
app.include_router(read_user)
app.include_router(update_user)
app.include_router(delete_user)

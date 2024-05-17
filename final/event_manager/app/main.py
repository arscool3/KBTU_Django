from fastapi import FastAPI
from database.database import engine,Base
# from models.models import User, Event, Venue, Category, Booking, Location
from routes.user_routes import user_router 
from routes.event_routes import event_router
from routes.venue_routes import venue_router
from routes.category_routes import router as category_router
from routes.booking_routes import router as booking_router
from tasks import archive_past_events

# Create tables in the database
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()
app.include_router(user_router)
app.include_router(event_router)
app.include_router(venue_router)
app.include_router(category_router)
app.include_router(booking_router)



@app.post("/api/archive_past_events")
async def trigger_archive_past_events():
    # Trigger the background task
    archive_past_events.send()
    return {"message": "Archiving past events task has been triggered."}
# Include routers and endpoints for your application
# Example: from .routers import user, event, etc.
# app.include_router(create_user)
# app.include_router(read_user)
# app.include_router(update_user)
# app.include_router(delete_user)

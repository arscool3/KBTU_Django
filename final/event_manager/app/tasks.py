import dramatiq
from datetime import datetime
from sqlalchemy.orm import Session
from database.database import get_db
from models.models import Event

@dramatiq.actor
def archive_past_events():
    db = next(get_db())
    past_events = db.query(Event).filter(Event.date_time < datetime.now()).all()
    for event in past_events:
        event.is_archived = True
    db.commit()
    db.close()

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional

from database.database import  get_db
from models.models import Event as DBEvent
from schemas.schemas import EventCreate, EventUpdate, Event
from crud.crud import( 
    get_by_id,
    get_all,
    create,
    update,
    delete
    )

event_router = APIRouter(prefix="/api/events", tags=["events"])


@event_router.get("/", response_model=List[Event])
def list_events(db: Session = Depends(get_db)):
    events = get_all(db, DBEvent )
    return events

@event_router.post("/", response_model=Event)
def new_event(event: EventCreate, db: Session = Depends(get_db)):
    return create(db, DBEvent, event)

@event_router.get("/{event_id}", response_model=Event)
def get_event_by_id(event_id: int, db: Session = Depends(get_db)):
    event = get_by_id(db, DBEvent, event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

@event_router.put("/{event_id}", response_model=Event)
def update_event_by_id(event_id: int, event_update: EventUpdate, db: Session = Depends(get_db)):
    updated_event = update(db,DBEvent, event_id, event_update)
    if not updated_event:
        raise HTTPException(status_code=404, detail="Event not found")
    return updated_event

@event_router.delete("/{event_id}", response_model=Event)
def delete_event_by_id(event_id: int, db: Session = Depends(get_db)):
    deleted_event = delete(db,DBEvent, event_id)
    if not deleted_event:
        raise HTTPException(status_code=404, detail="Event not found")
    return deleted_event

# ----------------------- Celery

# @event_router.post("/", response_model=Event)
# def new_event(event: EventCreate, db: Session = Depends(get_db)):
#     created_event = create_event_async.delay(event)  # Trigger Celery task
#     return created_event

# @event_router.put("/{event_id}", response_model=Event)
# def update_event_by_id(event_id: int, event_update: EventUpdate, db: Session = Depends(get_db)):
#     updated_event = update_event_async.delay(event_id, event_update)  # Trigger Celery task
#     return updated_event

# @event_router.delete("/{event_id}", response_model=Event)
# def delete_event_by_id(event_id: int, db: Session = Depends(get_db)):
#     deleted_event = delete_event_async.delay(event_id)  # Trigger Celery task
#     return deleted_event
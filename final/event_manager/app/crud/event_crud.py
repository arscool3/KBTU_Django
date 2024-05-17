# from sqlalchemy.orm import Session
# from models.models import Event as DBEvent
# from schemas.schemas import EventCreate, EventUpdate
# from typing import List

# def get_event(db: Session, event_id: int) -> DBEvent:
#     return db.query(DBEvent).filter(DBEvent.id == event_id).first()

# def get_all_events(db: Session) -> List[DBEvent]:
#     return db.query(DBEvent).all()

# def create_event(db: Session, event: EventCreate) -> DBEvent:
#     db_event = DBEvent(**event.dict())
#     db.add(db_event)
#     db.commit()
#     db.refresh(db_event)
#     return db_event

# def update_event(db: Session, event_id: int, event_update: EventUpdate) -> DBEvent:
#     db_event = get_event(db, event_id)
#     if db_event:
#         for field, value in event_update.dict(exclude_unset=True).items():
#             setattr(db_event, field, value)
#         db.commit()
#         db.refresh(db_event)
#     return db_event

# def delete_event(db: Session, event_id: int) -> DBEvent:
#     db_event = get_event(db, event_id)
#     if db_event:
#         db.delete(db_event)
#         db.commit()
#     return db_event

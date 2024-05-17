# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from schemas.schemas import VenueCreate, Venue as VenueSchema
# from database.database import SessionLocal
# from models.models import Venue

# router = APIRouter(prefix="/api/venues", tags=["venues"])

# def get_venue_by_id(db: Session, venue_id: int):
#     return db.query(Venue).filter(Venue.id == venue_id).first()

# def get_all_venues(db: Session):
#     return db.query(Venue).all()

# def create_venue(db: Session, venue: VenueCreate):
#     db_venue = Venue(**venue.dict())
#     db.add(db_venue)
#     db.commit()
#     db.refresh(db_venue)
#     return db_venue

# def update_venue(db: Session, venue_id: int, venue_data: VenueCreate):
#     db_venue = get_venue_by_id(db, venue_id)
#     if db_venue:
#         for key, value in venue_data.dict().items():
#             setattr(db_venue, key, value)
#         db.commit()
#         db.refresh(db_venue)
#     return db_venue

# def delete_venue(db: Session, venue_id: int):
#     db_venue = get_venue_by_id(db, venue_id)
#     if db_venue:
#         db.delete(db_venue)
#         db.commit()
#         return db_venue
#     return None

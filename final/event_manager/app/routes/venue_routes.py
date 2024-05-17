from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.schemas import VenueCreate, Venue as VenueSchema
from models.models import Venue as DBVenue
from database.database import get_db
from crud.crud import( 
    get_by_id,
    get_all,
    create,
    update,
    delete
    )

venue_router = APIRouter(prefix="/api/venues", tags=["venues"])

@venue_router.get("/", response_model=list[VenueSchema])
def list_venues(db: Session = Depends(get_db)):
    venues = get_all(db,DBVenue)
    return venues

@venue_router.post("/", response_model=VenueSchema)
def create_new_venue(venue: VenueCreate, db: Session = Depends(get_db)):
    return create(db, DBVenue, venue)

@venue_router.get("/{venue_id}", response_model=VenueSchema)
def get_venue(venue_id: int, db: Session = Depends(get_db)):
    db_venue = get_by_id(db,DBVenue, venue_id)
    if db_venue is None:
        raise HTTPException(status_code=404, detail="Venue not found")
    return db_venue

@venue_router.put("/{venue_id}", response_model=VenueSchema)
def update_venue_details(venue_id: int, venue: VenueCreate, db: Session = Depends(get_db)):
    updated_venue = update(db,DBVenue, venue_id, venue)
    if updated_venue is None:
        raise HTTPException(status_code=404, detail="Venue not found")
    return updated_venue

@venue_router.delete("/{venue_id}", response_model=VenueSchema)
def delete_venue_by_id(venue_id: int, db: Session = Depends(get_db)):
    deleted_venue = delete(db,DBVenue, venue_id)
    if deleted_venue is None:
        raise HTTPException(status_code=404, detail="Venue not found")
    return deleted_venue

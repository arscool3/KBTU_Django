from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.models import Booking as DBBooking
from database.database import get_db
from schemas.schemas import BookingCreate, Booking
from crud.crud import( 
    get_by_id,
    get_all,
    create,
    update,
    delete
    )
router = APIRouter(prefix="/api/bookings", tags=["bookings"])

@router.post("/", response_model=Booking)
def create_new_booking(booking: BookingCreate, db: Session = Depends(get_db)):
    return create(db,DBBooking, booking)

@router.get("/", response_model=List[Booking])
def get_bookings( db: Session = Depends(get_db)):
    db_bookings = get_all(db, DBBooking)

    return db_bookings

@router.get("/{booking_id}", response_model=Booking)
def get_booking_by_id(booking_id: int, db: Session = Depends(get_db)):
    db_booking = get_by_id(db,DBBooking, booking_id)
    if db_booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    return db_booking

@router.put("/{booking_id}", response_model=Booking)
def update_existing_booking(booking_id: int, booking_update: Booking, db: Session = Depends(get_db)):
    db_booking = update(db,DBBooking, booking_id, booking_update)
    if db_booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    return db_booking

@router.delete("/{booking_id}", response_model=Booking)
def delete_existing_booking(booking_id: int, db: Session = Depends(get_db)):
    db_booking = delete(db, DBBooking, booking_id)
    if db_booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    return db_booking

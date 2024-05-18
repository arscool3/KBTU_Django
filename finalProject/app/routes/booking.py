from fastapi import APIRouter, Depends, HTTPException, status
from app.models import Booking, User, Seat
from app.db import get_db
from sqlalchemy.orm import Session
from app.routes.auth import get_current_user
from app.schemas import BookingResponse

router = APIRouter()


@router.get("/users/{user_id}/bookings",
            dependencies=[Depends(get_current_user)])  # Add get_current_user for authentication
async def get_user_bookings(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    bookings = db.query(Booking).filter(Booking.user_id == user_id).all()
    return bookings


@router.get("/{booking_id}", response_model=BookingResponse)
async def get_booking(booking_id: int, db: Session = Depends(get_db)):
    booking = db.query(Booking).filter(Booking.id == booking_id).first()
    if not booking:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Booking not found")
    return booking


@router.post("/", response_model=BookingResponse,
             dependencies=[Depends(get_current_user)])  # Add get_current_user for authentication
async def create_booking(booking: Booking, current_user: User = Depends(get_current_user),
                         db: Session = Depends(get_db)):
    # Check if user is authenticated (through get_current_user dependency)

    # Validate seat availability
    seat = db.query(Seat).filter(Seat.id == booking.seat_id).first()
    if not seat:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Seat not found")
    if seat.schedule_id is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Seat is not associated with a schedule")

    # Check for existing booking for the same seat and schedule
    existing_booking = db.query(Booking).filter(
        Booking.seat_id == booking.seat_id, Booking.schedule_id == seat.schedule_id
    ).first()
    if existing_booking:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Seat is already booked for this schedule")

    booking.user_id = current_user.id
    db.add(booking)
    db.commit()
    db.refresh(booking)
    return booking


@router.put("/{booking_id}", response_model=BookingResponse,
            dependencies=[Depends(get_current_user)])  # Add get_current_user for authentication
async def update_booking(booking_id: int, booking_data: Booking, db: Session = Depends(get_db)):
    booking = db.query(Booking).filter(Booking.id == booking_id).first()
    if not booking:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Booking not found")

    # Optional: Check if user owns the booking (consider adding a user_id to Booking)
    # ...

    booking.update(booking_data.dict(exclude_unset=True))
    db.commit()
    db.refresh(booking)
    return booking


@router.delete("/{booking_id}", dependencies=[Depends(get_current_user)])  # Add get_current_user for authentication
async def delete_booking(booking_id: int, db: Session = Depends(get_db)):
    booking = db.query(Booking).filter(Booking.id == booking_id).first()
    if not booking:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Booking not found")

    # Optional: Check if user owns the booking
    # ...

    db.delete(booking)
    db.commit()
    return {"message": "Booking deleted successfully"}

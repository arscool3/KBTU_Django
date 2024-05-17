from fastapi import APIRouter, Depends, HTTPException, status
from app.models import Schedule, Seat
from app.db import get_db
from sqlalchemy import Session
from app.routes.auth import get_current_user

router = APIRouter()


@router.get("/schedules/{schedule_id}/seats",
            dependencies=[Depends(get_current_user)])  # Add get_current_user for authentication (optional)
async def get_seats(schedule_id: int, db: Session = Depends(get_db)):
    schedule = db.query(Schedule).filter(Schedule.id == schedule_id).first()
    if not schedule:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Schedule not found")

    seats = db.query(Seat).filter(Seat.schedule_id == schedule_id).all()
    return seats


@router.post("/schedules/{schedule_id}/seats",
             dependencies=[Depends(get_current_user)])  # Add get_current_user for authentication
async def create_seat(seat: Seat, schedule_id: int, db: Session = Depends(get_db)):
    schedule = db.query(Schedule).filter(Schedule.id == schedule_id).first()
    if not schedule:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Schedule not found")

    # Validate unique seat number for the schedule
    existing_seat = db.query(Seat).filter(Seat.schedule_id == schedule_id, Seat.seat_number == seat.seat_number).first()
    if existing_seat:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Seat number already exists for this schedule")

    seat.schedule_id = schedule_id
    db.add(seat)
    db.commit()
    db.refresh(seat)
    return seat


@router.get("/{seat_id}")  # No get_current_user dependency (optional for some)
async def get_seat(seat_id: int, db: Session = Depends(get_db)):
    seat = db.query(Seat).filter(Seat.id == seat_id).first()
    if not seat:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Seat not found")
    return seat

@router.put("/{seat_id}", dependencies=[Depends(get_current_user)])  # Add get_current_user for authentication
async def update_seat(seat_id: int, seat_data: Seat, db: Session = Depends(get_db)):
    seat = db.query(Seat).filter(Seat.id == seat_id).first()
    if not seat:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Seat not found")

    # Validate unique seat number for the schedule (if updated)
    if "seat_number" in seat_data.dict() and seat_data.seat_number:
        existing_seat = db.query(Seat).filter(
            Seat.schedule_id == seat.schedule_id, Seat.seat_number == seat_data.seat_number
        ).first()
        if existing_seat and existing_seat.id != seat.id:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Seat number already exists for this schedule")

    seat.update(seat_data.dict(exclude_unset=True))
    db.commit()
    db.refresh(seat)
    return seat


@router.delete("/{seat_id}", dependencies=[Depends(get_current_user)])  # Add get_current_user for authentication (optional)
async def delete_seat(seat_id: int, db: Session = Depends(get_db)):
    seat = db.query(Seat).filter(Seat.id == seat_id).first()
    if not seat:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Seat not found")

    # Optional: Check user permissions before deletion (e.g., is user an admin?)
    # ... (e.g., check if user owns the booking for this seat)

    db.delete(seat)
    db.commit()
    return {"message": "Seat deleted successfully"}
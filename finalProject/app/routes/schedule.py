from fastapi import APIRouter, Depends, HTTPException, status
from app.models import Schedule, Bus, Route
from app.db import get_db
from sqlalchemy import Session
from app.routes.auth import get_current_user
from app.schemas import ScheduleResponse

router = APIRouter()


@router.get("/", dependencies=[Depends(get_current_user)])  # Add get_current_user for authentication (optional)
async def get_schedules(db: Session = Depends(get_db)):
    schedules = db.query(Schedule).all()
    return schedules


@router.post("/", response_model= ScheduleResponse,  dependencies=[Depends(get_current_user)])  # Add get_current_user for authentication
async def create_schedule(schedule: Schedule, db: Session = Depends(get_db)):
    # Check if bus and route exist
    bus = db.query(Bus).filter(Bus.id == schedule.bus_id).first()
    route = db.query(Route).filter(Route.id == schedule.route_id).first()
    if not bus or not route:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid bus or route ID")

    db.add(schedule)
    db.commit()
    db.refresh(schedule)
    return schedule

@router.get("/{schedule_id}",response_model= ScheduleResponse, dependencies=[Depends(get_current_user)])  # Add get_current_user for authentication (optional)
async def get_schedule(schedule_id: int, db: Session = Depends(get_db)):
    schedule = db.query(Schedule).filter(Schedule.id == schedule_id).first()
    if not schedule:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Schedule not found")
    return schedule


@router.put("/{schedule_id}",response_model= ScheduleResponse, dependencies=[Depends(get_current_user)])  # Add get_current_user for authentication (optional)
async def update_schedule(schedule_id: int, schedule_data: Schedule, db: Session = Depends(get_db)):
    schedule = db.query(Schedule).filter(Schedule.id == schedule_id).first()
    if not schedule:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Schedule not found")

    # Check if bus and route still exist (optional)
    # ...

    schedule.update(schedule_data.dict(exclude_unset=True))
    db.commit()
    db.refresh(schedule)
    return schedule


@router.delete("/{schedule_id}", dependencies=[Depends(get_current_user)])  # Add get_current_user for authentication (optional)
async def delete_schedule(schedule_id: int, db: Session = Depends(get_db)):
    schedule = db.query(Schedule).filter(Schedule.id == schedule_id).first()
    if not schedule:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Schedule not found")

    # Optional: Check user permissions before deletion (e.g., is user an admin?)

    db.delete(schedule)
    db.commit()
    return {"message": "Schedule deleted successfully"}
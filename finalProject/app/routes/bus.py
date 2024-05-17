from fastapi import APIRouter, Depends, HTTPException, status
from app.models import Bus
from app.db import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from typing import List
from app.routes.auth import get_current_user
from app.schemas import BusResponse, BusCreate

router = APIRouter()


@router.get("/", dependencies=[Depends(get_current_user)])  # Add get_current_user for authentication
async def get_buses(db: Session = Depends(get_db)):
    buses = db.query(Bus).all()
    return buses


@router.post("/", response_model=BusResponse, dependencies=[Depends(get_current_user)])  # Add get_current_user for authentication
async def create_bus(bus: BusCreate, db: Session = Depends(get_db)):
    db_bus = Bus(**bus.dict())
    db.add(db_bus)
    db.commit()
    db.refresh(db_bus)
    return db_bus


@router.get("/{bus_id}", response_model=BusResponse, dependencies=[Depends(get_current_user)])  # Add get_current_user for authentication
async def get_bus(bus_id: int, db: Session = Depends(get_db)):
    bus = db.query(Bus).filter(Bus.id == bus_id).first()
    if not bus:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Bus not found")
    return bus


@router.put("/{bus_id}", response_model=BusResponse, dependencies=[Depends(get_current_user)])  # Add get_current_user for authentication
async def update_bus(bus_id: int, bus_data: BusCreate, db: Session = Depends(get_db)):
    bus = db.query(Bus).filter(Bus.id == bus_id).first()
    if not bus:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Bus not found")

    bus.update(bus_data.dict(exclude_unset=True))
    db.commit()
    db.refresh(bus)
    return bus


@router.delete("/{bus_id}", dependencies=[Depends(get_current_user)])  # Add get_current_user for authentication
async def delete_bus(bus_id: int, db: Session = Depends(get_db)):
    bus = db.query(Bus).filter(Bus.id == bus_id).first()
    if not bus:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Bus not found")

    # Optional: Check user permissions before deletion (e.g., is user an admin?)

    db.delete(bus)
    db.commit()
    return {"message": "Bus deleted successfully"}

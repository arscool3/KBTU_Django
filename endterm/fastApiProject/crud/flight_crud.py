from sqlalchemy.orm import Session
from models import Flight
from schemas import FlightCreate, FlightUpdate


def get_flights(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Flight).offset(skip).limit(limit).all()


def get_flight(db: Session, flight_id: int):
    return db.query(Flight).filter(Flight.id == flight_id).first()


def create_flight(db: Session, flight: FlightCreate):
    db_flight = Flight(**flight.dict())
    db.add(db_flight)
    db.commit()
    db.refresh(db_flight)
    return db_flight


def update_flight(db: Session, flight_id: int, flight: FlightUpdate):
    db_flight = db.query(Flight).filter(Flight.id == flight_id).first()
    if db_flight:
        for key, value in flight.dict().items():
            setattr(db_flight, key, value)
        db.commit()
        db.refresh(db_flight)
    return db_flight


def delete_flight(db: Session, flight_id: int):
    db_flight = db.query(Flight).filter(Flight.id == flight_id).first()
    if db_flight:
        db.delete(db_flight)
        db.commit()
    return db_flight
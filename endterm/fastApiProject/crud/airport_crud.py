# crud.py

from sqlalchemy.orm import Session
from models import Airport
from schemas import AirportCreate

def get_airport(db: Session, airport_id: int):
    return db.query(Airport).filter(Airport.id == airport_id).first()

def get_airports(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Airport).offset(skip).limit(limit).all()

def create_airport(db: Session, airport: AirportCreate):
    db_airport = Airport(**airport.dict())
    db.add(db_airport)
    db.commit()
    db.refresh(db_airport)
    return db_airport

def update_airport(db: Session, airport_id: int, airport: AirportCreate):
    db_airport = db.query(Airport).filter(Airport.id == airport_id).first()
    if db_airport:
        for key, value in airport.dict().items():
            setattr(db_airport, key, value)
        db.commit()
        db.refresh(db_airport)
    return db_airport

def delete_airport(db: Session, airport_id: int):
    db_airport = db.query(Airport).filter(Airport.id == airport_id).first()
    if db_airport:
        db.delete(db_airport)
        db.commit()
    return db_airport

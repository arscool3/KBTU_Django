# crud.py
from sqlalchemy import update
from sqlalchemy.orm import Session
from models import City
from schemas import CityCreate

def get_city(db: Session, city_id: int):
    return db.query(City).filter(City.id == city_id).first()

def get_cities(db: Session, skip: int = 0, limit: int = 10):
    return db.query(City).offset(skip).limit(limit).all()

def create_city(db: Session, city: CityCreate):
    db_city = City(**city.dict())
    db.add(db_city)
    db.commit()
    db.refresh(db_city)
    return db_city

def update_city(db: Session, city_id: int, city: CityCreate):
    db_city = db.query(City).filter(City.id == city_id).first()
    if db_city:
        stmt = (
            update(City).
            where(City.id == city_id).
            values(**city.dict())
        )
        db.execute(stmt)
        db.commit()
        db.refresh(db_city)
    return db_city

def delete_city(db: Session, city_id: int):
    db_city = db.query(City).filter(City.id == city_id).first()
    if db_city:
        db.delete(db_city)
        db.commit()
    return db_city

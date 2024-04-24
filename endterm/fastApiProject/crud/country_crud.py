# crud.py

from sqlalchemy.orm import Session
from models import Country
from schemas import CountryCreate

def get_country(db: Session, country_id: int):
    return db.query(Country).filter(Country.id == country_id).first()

def get_countries(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Country).offset(skip).limit(limit).all()

def create_country(db: Session, country: CountryCreate):
    db_country = Country(name=country.name)
    db.add(db_country)
    db.commit()
    db.refresh(db_country)
    return db_country

def update_country(db: Session, country_id: int, country: CountryCreate):
    db_country = db.query(Country).filter(Country.id == country_id).first()
    if db_country:
        for key, value in country.dict().items():
            setattr(db_country, key, value)
        db.commit()
        db.refresh(db_country)
    return db_country

def delete_country(db: Session, country_id: int):
    db_country = db.query(Country).filter(Country.id == country_id).first()
    if db_country:
        db.delete(db_country)
        db.commit()
    return db_country

# Similar functions for City and Airport models...

# crud.py
from sqlalchemy.orm import Session
import models
import schemas

# Function to seed data
def seed_data(db: Session):
    # Seed your data here using SQLAlchemy ORM or raw SQL queries
    pass

# CRUD operations for Seed entity
def create_seed(db: Session, seed: schemas.SeedCreate):
    db_seed = models.Seed(**seed.dict())
    db.add(db_seed)
    db.commit()
    db.refresh(db_seed)
    return db_seed

def get_seeds(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Seed).offset(skip).limit(limit).all()

def get_seed(db: Session, seed_id: int):
    return db.query(models.Seed).filter(models.Seed.id == seed_id).first()

def update_seed(db: Session, seed_id: int, seed: schemas.SeedUpdate):
    db_seed = db.query(models.Seed).filter(models.Seed.id == seed_id).first()
    if db_seed:
        for var, value in vars(seed).items():
            if value is not None:
                setattr(db_seed, var, value)
        db.commit()
        db.refresh(db_seed)
        return db_seed
    else:
        return None

def delete_seed(db: Session, seed_id: int):
    db_seed = db.query(models.Seed).filter(models.Seed.id == seed_id).first()
    if db_seed:
        db.delete(db_seed)
        db.commit()
        return {"message": "Seed deleted successfully"}
    else:
        return {"message": "Seed not found"}
# crud.py
def verify_token(token: str):
    # Dummy implementation, replace it with your actual token verification logic
    return token == "valid_token"

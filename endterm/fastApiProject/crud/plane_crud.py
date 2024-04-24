from sqlalchemy.orm import Session
from models import Plane
from schemas import PlaneCreate


def get_plane(db: Session, plane_id: int):
    return db.query(Plane).filter(Plane.id == plane_id).first()


def get_planes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Plane).offset(skip).limit(limit).all()


def create_plane(db: Session, plane: PlaneCreate):
    db_plane = Plane(**plane.dict())
    db.add(db_plane)
    db.commit()
    db.refresh(db_plane)
    return db_plane


def update_plane(db: Session, plane_id: int, plane: PlaneCreate):
    db_plane = db.query(Plane).filter(Plane.id == plane_id).first()
    if db_plane:
        for key, value in plane.dict().items():
            setattr(db_plane, key, value)
        db.commit()
        db.refresh(db_plane)
    return db_plane


def delete_plane(db: Session, plane_id: int):
    db_plane = db.query(Plane).filter(Plane.id == plane_id).first()
    if db_plane:
        db.delete(db_plane)
        db.commit()
    return db_plane

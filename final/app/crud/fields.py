from sqlalchemy.orm import Session
import models
from fastapi import HTTPException, status


def create_field(db: Session, name: str):
    field = models.Field(name=name)
    db.add(field)
    db.commit()
    db.refresh(field)
    return field

def get_field(db: Session, field_id: int):
    return db.query(models.Field).filter(models.Field.id == field_id).first()

def get_fields(db: Session):
    return db.query(models.Field).all()

def delete_field(db: Session, field_id: int):
    field = db.query(models.Field).filter(models.Field.id == field_id).first()
    if field:
        db.delete(field)
        db.commit()
        return 'OK'
    raise HTTPException(status_code=404, detail="Field not found")



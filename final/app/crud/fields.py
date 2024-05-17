from sqlalchemy.orm import Session
from models import Field

def create_field(db: Session, name: str):
    field = Field(name=name)
    db.add(field)
    db.commit()
    db.refresh(field)
    return field

def get_field(db: Session, field_id: int):
    return db.query(Field).filter(Field.id == field_id).first()

def update_field(db: Session, field_id: int, name: str):
    field = db.query(Field).filter(Field.id == field_id).first()
    if field:
        field.name = name
        db.commit()
        db.refresh(field)
        return field
    return None

def delete_field(db: Session, field_id: int):
    field = db.query(Field).filter(Field.id == field_id).first()
    if field:
        db.delete(field)
        db.commit()
        return True
    return False


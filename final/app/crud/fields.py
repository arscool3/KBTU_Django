from sqlalchemy.orm import Session
import models

def create_field(db: Session, name: str):
    field = models.Field(name=name)
    db.add(field)
    db.commit()
    db.refresh(field)
    return field

def get_field(db: Session, field_id: int):
    return db.query(models.Field).filter(models.Field.id == field_id).first()

def get_papers_by_field(db: Session, field_id: int):
    field = db.query(models.Field).filter(models.Field.id == field_id).first()
    if field:
        return field.papers
    return []

def delete_field(db: Session, field_id: int):
    field = db.query(models.Field).filter(models.Field.id == field_id).first()
    if field:
        db.delete(field)
        db.commit()
        return True
    return False


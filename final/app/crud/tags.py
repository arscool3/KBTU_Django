from sqlalchemy.orm import Session
from models import Tag
from fastapi import HTTPException, status


def create_tag(db: Session, name: str):
    tag = Tag(name=name)
    db.add(tag)
    db.commit()
    db.refresh(tag)
    return tag

def get_tag(db: Session, tag_id: int):
    return db.query(Tag).filter(Tag.id == tag_id).first()

def get_tags(db: Session):
    return db.query(Tag).all()

def delete_tag(db: Session, tag_id: int):
    tag = db.query(Tag).filter(Tag.id == tag_id).first()
    if tag:
        db.delete(tag)
        db.commit()
        return 'OK'
    raise HTTPException(status_code=404, detail="Field not found")



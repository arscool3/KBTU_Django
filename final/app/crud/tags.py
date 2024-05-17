from sqlalchemy.orm import Session
from models import Tag

def create_tag(db: Session, name: str):
    tag = Tag(name=name)
    db.add(tag)
    db.commit()
    db.refresh(tag)
    return tag

def get_tag(db: Session, tag_id: int):
    return db.query(Tag).filter(Tag.id == tag_id).first()

def update_tag(db: Session, tag_id: int, name: str):
    tag = db.query(Tag).filter(Tag.id == tag_id).first()
    if tag:
        tag.name = name
        db.commit()
        db.refresh(tag)
        return tag
    return None

def delete_tag(db: Session, tag_id: int):
    tag = db.query(Tag).filter(Tag.id == tag_id).first()
    if tag:
        db.delete(tag)
        db.commit()
        return True
    return False


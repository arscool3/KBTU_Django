from sqlalchemy.orm import Session
from fastapi import HTTPException, status
import models
import schemas


def get_paper(db: Session, paper_id: int):
    return db.query(models.Paper).filter(models.Paper.id == paper_id).first()

def create_paper(db: Session, paper: schemas.PaperCreate, user_id: int):
    db_paper = models.Paper(**paper.dict(), author_id=user_id)
    db.add(db_paper)
    db.commit()
    db.refresh(db_paper)
    return db_paper

def update_paper(db: Session, paper_id: int, paper: schemas.PaperCreate,  user_id: int):
    db_paper = db.query(models.Paper).filter(models.Paper.id == paper_id).first()
    if not db_paper:
        raise HTTPException(status_code=404, detail="Paper not found")
    if db_paper.author_id != user_id:
        raise HTTPException(status_code=403, detail="Do not have premission to delete")
    for key, value in paper.dict().items():
        setattr(db_paper, key, value)
    db.commit()
    db.refresh(db_paper)
    return db_paper

def delete_paper(db: Session, paper_id: int, user_id: int):
    db_paper = db.query(models.Paper).filter(models.Paper.id == paper_id).first()
    if db_paper.author_id != user_id:
        raise HTTPException(status_code=403, detail="Do not have premission to delete")
    if db_paper:
        db.delete(db_paper)
        db.commit()

def get_papers(db: Session, tag_ids: list[int], field_ids: list[int], skip: int = 0, limit: int = 10):
    query = db.query(models.Paper)
    if tag_ids:
        query = query.filter(models.Paper.tags.any(models.Tag.id.in_(tag_ids)))
    if field_ids:
        query = query.filter(models.Paper.fields.any(models.Field.id.in_(field_ids)))
    papers = query.offset(skip).limit(limit).all()
    return papers

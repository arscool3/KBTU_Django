from sqlalchemy.orm import Session
from fastapi import HTTPException, status
import models
import schemas


def _tag_filed_ids2orm(db: Session, paper, user_id):
    tag_ids = paper.tags
    paper.tags = []
    field_ids = paper.fields
    paper.fields = []
    db_paper = models.Paper(**paper.dict(), author_id=user_id)
    db_paper.tags = [db.query(models.Tag).get(tag_id) for tag_id in tag_ids]
    db_paper.fields = [db.query(models.Field).get(field_id) for field_id in field_ids]
    return db_paper

def get_paper(db: Session, paper_id: int):
    return db.query(models.Paper).filter(models.Paper.id == paper_id).first()

def create_paper(db: Session, paper: schemas.PaperCreate, user_id: int):
    db_paper = _tag_filed_ids2orm(db, paper, user_id)
    db.add(db_paper)
    db.commit()
    db.refresh(db_paper)
    return db_paper

def update_paper(db: Session, paper_id: int, paper: schemas.PaperUpdate,  user_id: int):
    db_paper = db.query(models.Paper).filter(models.Paper.id == paper_id).first()
    if not db_paper:
        raise HTTPException(status_code=404, detail="Paper not found")
    if db_paper.author_id != user_id:
        raise HTTPException(status_code=403, detail="Do not have premission to delete")
    if paper.title:
        db_paper.title = paper.title
    if paper.abstract:
        db_paper.abstract = paper.abstract
    if paper.tags:
        db_paper.tags.clear()
        db_paper.tags = [db.query(models.Tag).get(tag_id) for tag_id in paper.tags]
    if paper.fields:
        db_paper.fields.clear()
        db_paper.fields = [db.query(models.Field).get(field_id) for field_id in paper.fields]
    db.commit()
    db.refresh(db_paper)
    return db_paper

def delete_paper(db: Session, paper_id: int, user_id: int):
    db_paper = db.query(models.Paper).filter(models.Paper.id == paper_id).first()
    if db_paper.author_id != user_id:
        raise HTTPException(status_code=403, detail="Do not have premission to delete")
    if not db_paper:
        raise HTTPException(status_code=404, detail="Paper not found")
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

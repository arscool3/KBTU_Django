from sqlalchemy.orm import Session
import models
import schemas


def get_paper(db: Session, paper_id: int):
    return db.query(models.Paper).filter(models.Paper.id == paper_id).first()

def get_papers(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Paper).offset(skip).limit(limit).all()

def create_paper(db: Session, paper: schemas.PaperCreate, user_id: int):
    db_paper = models.Paper(**paper.dict(), author_id=user_id)
    db.add(db_paper)
    db.commit()
    db.refresh(db_paper)
    return db_paper

def update_paper(db: Session, paper_id: int, paper: schemas.PaperCreate):
    db_paper = db.query(models.Paper).filter(models.Paper.id == paper_id).first()
    if not db_paper:
        return None
    for key, value in paper.dict().items():
        setattr(db_paper, key, value)
    db.commit()
    db.refresh(db_paper)
    return db_paper

def delete_paper(db: Session, paper_id: int):
    db_paper = db.query(models.Paper).filter(models.Paper.id == paper_id).first()
    if db_paper:
        db.delete(db_paper)
        db.commit()



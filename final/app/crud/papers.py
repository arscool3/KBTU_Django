from sqlalchemy.orm import Session
from models import Paper

def create_paper(db: Session, title: str, abstract: str, file_path: str, author_id: int, tag_ids: list, field_ids: list):
    paper = Paper(title=title, abstract=abstract, file_path=file_path, author_id=author_id)

    for tag_id in tag_ids:
        tag = db.query(Tag).filter(Tag.id == tag_id).first()
        if tag:
            paper.tags.append(tag)

    for field_id in field_ids:
        field = db.query(Field).filter(Field.id == field_id).first()
        if field:
            paper.fields.append(field)

    db.add(paper)
    db.commit()
    db.refresh(paper)
    return paper

def get_paper(db: Session, paper_id: int):
    return db.query(Paper).filter(Paper.id == paper_id).first()

def update_paper(db: Session, paper_id: int, title: str, abstract: str, file_path: str,  tag_ids: list, field_ids: list):
    paper = get_paper(Session, paper_id)
    if paper:
        paper.title = title
        paper.abstract = abstract
        paper.file_path = file_path

        paper.tags.clear()
        for tag_id in tag_ids:
            tag = db.query(Tag).filter(Tag.id == tag_id).first()
            if tag:
                paper.tags.append(tag)

        paper.fields.clear()
        for field_id in field_ids:
            field = db.query(Field).filter(Field.id == field_id).first()
            if field:
                paper.fields.append(field)

        db.commit()
        db.refresh(paper)
        return paper
    return None

def delete_paper(db: Session, paper_id: int):
    paper = db.query(Paper).filter(Paper.id == paper_id).first()
    if paper:
        db.delete(paper)
        db.commit()
        return True
    return False


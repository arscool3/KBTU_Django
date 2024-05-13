from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.models.book import Author
from app.schemas.author import AuthorCreate

router = APIRouter()


@router.post("/authors/")
def create_author(author: AuthorCreate, db: Session = Depends(get_db)):
    db_author = Author()
    db_author.name = author.name
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

@router.get("/authors/")
def read_authors(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Author).offset(skip).limit(limit).all()

@router.get("/authors/{author_id}")
def read_author(author_id: int, db: Session = Depends(get_db)):
    db_author = db.query(Author).filter(Author.id == author_id).first()
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return db_author

@router.delete("/authors/{author_id}")
def delete_author(author_id: int, db: Session = Depends(get_db)):
    db_author = db.query(Author).filter(Author.id == author_id).first()
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    db.delete(db_author)
    db.commit()
    return {"message": "Author deleted successfully"}
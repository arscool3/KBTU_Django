from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from crud.papers import *
from crud.users import get_current_user
from db import get_db
from models import Paper
from schemas import PaperCreate, PaperUpdate

router = APIRouter()

@router.post("/papers", response_model=Paper)
def create_paper_route(paper_create: PaperCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_paper(db=db, paper=paper_create, user_id = current_user.id)

@router.get("/papers/{paper_id}", response_model=Paper)
def get_paper_route(paper_id: int, db: Session = Depends(get_db)):
    paper = get_paper_by_id(db=db, paper_id=paper_id)
    if paper is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Paper not found")
    return paper

@router.get("/papers", response_model=list[Paper])
def get_papers_route(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_papers(db=db, skip=skip, limit=limit)

@router.put("/papers/{paper_id}", response_model=Paper)
def update_paper_route(paper_id: int, paper_update: PaperUpdate, db: Session = Depends(get_db)):
    return update_paper(db=db, paper_id=paper_id, paper_update=paper_update)

@router.delete("/papers/{paper_id}")
def delete_paper_route(paper_id: int, db: Session = Depends(get_db)):
    deleted = delete_paper(db=db, paper_id=paper_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Paper not found")
    return {"message": "Paper deleted successfully"}


from fastapi import APIRouter, Depends, HTTPException, status, Query
from typing import Annotated
from sqlalchemy.orm import Session
from crud.papers import *
from crud.users import get_current_user
from db import get_db
from models import User
from schemas import PaperCreate, Paper, PaperUpdate
from typing import Optional, List

router = APIRouter()


class CommonQueryParams:
    def __init__(self, paper_id: int, token: str):
        self.paper_id = paper_id
        self.token = token


@router.post("/papers", response_model=Paper, status_code=status.HTTP_201_CREATED)
def create_paper_route(paper_create: PaperCreate, token: str, db: Session = Depends(get_db)):
    current_user = get_current_user(db, token)
    return create_paper(db=db, paper=paper_create, user_id = current_user.id)


@router.get("/papers/{paper_id}", response_model=Paper)
def get_paper_route(paper_id: int, db: Session = Depends(get_db)):
    paper = get_paper(db=db, paper_id=paper_id)
    if paper is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Paper not found")
    return paper


@router.get("/papers", response_model=List[Paper])
def get_papers_route(
    tag_ids: Optional[List[int]] = Query(None),
    field_ids: Optional[List[int]] = Query(None),
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    if tag_ids is None:
        tag_ids = []
    if field_ids is None:
        field_ids = []

    papers = get_papers(db, tag_ids, field_ids, skip, limit)
    return papers

@router.put("/papers/{paper_id}", response_model=Paper)
def update_paper_route(commons: Annotated[CommonQueryParams, Depends(CommonQueryParams)], paper_update: PaperUpdate, db: Session = Depends(get_db)):
    current_user = get_current_user(db, commons.token)
    return update_paper(db=db, paper_id=commons.paper_id, paper=paper_update, user_id = current_user.id)


@router.delete("/papers/{paper_id}")
def delete_paper_route(commons: Annotated[CommonQueryParams, Depends(CommonQueryParams)], db: Session = Depends(get_db)):
    current_user = get_current_user(db, commons.token)
    delete_paper(db=db, paper_id=commons.paper_id, user_id = current_user.id)
    return {"message": "Paper deleted successfully"}


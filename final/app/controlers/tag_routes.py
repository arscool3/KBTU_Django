from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from db import get_db
from crud.tags import *
import schemas

router = APIRouter()

@router.post("/tags", response_model=schemas.Tag ,status_code=status.HTTP_201_CREATED)
def create_new_tag(name: str, db: Session = Depends(get_db)):
    return create_tag(db, name)

@router.get("/tags/{tag_id}")
def read_tag(tag_id: int, db: Session = Depends(get_db)):
    db_tag = get_tag(db, tag_id)
    if db_tag is None:
        raise HTTPException(status_code=404, detail="Tag not found")
    return db_tag.name

@router.get("/tags", response_model=List[schemas.Tag])
def read_tags(db: Session = Depends(get_db)):
    return get_tags(db)

@router.delete("/tags/{tag_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_existing_tag(tag_id: int, db: Session = Depends(get_db)):
    delete_tag(db, tag_id)
    return {"detail": "Tag deleted"}


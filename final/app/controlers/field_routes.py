from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from db import get_db
from schemas import Field
from crud.fields import *

router = APIRouter()

@router.post("/fields", response_model=Field, status_code=status.HTTP_201_CREATED)
def create_new_field(name: str , db: Session = Depends(get_db)):
    return create_field(db, name)

@router.get("/fields/{field_id}", response_model=Field)
def read_field(field_id: int, db: Session = Depends(get_db)):
    db_field = get_field(db, field_id)
    if db_field is None:
        raise HTTPException(status_code=404, detail="Field not found")
    return db_field

@router.get("/fields", response_model=List[Field])
def read_fields(db: Session = Depends(get_db)):
    return get_fields(db)

@router.delete("/fields/{field_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_existing_field(field_id: int, db: Session = Depends(get_db)):
    delete_field(db, field_id)
    return {"detail": "Field deleted"}


from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, crud, database

router = APIRouter()

@router.post("/books/", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(database.get_db)):
    return crud.create_book(db, book)

@router.get("/books/", response_model=list[schemas.Book])
async def get_books(db: Session = Depends(database.engine)):
    return crud.get_books(db)

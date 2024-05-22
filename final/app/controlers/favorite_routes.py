from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from db import get_db
import crud.favorite as crud
from crud.users import get_current_user
import models
import schemas

router = APIRouter()


@router.post("/favorites/", response_model=schemas.Favorite, status_code=status.HTTP_201_CREATED)
def create_favorite(token: str, favorite: schemas.FavoriteCreate, db: Session = Depends(get_db)):
    current_user = get_current_user(db, token)
    return crud.create_favorite(user_id = current_user.id, db=db, favorite=favorite)

@router.get("/favorites/{favorite_id}", response_model=schemas.Favorite)
def read_favorite(favorite_id: int, db: Session = Depends(get_db)):
    db_favorite = crud.get_favorite(db=db, favorite_id=favorite_id)
    if db_favorite is None:
        raise HTTPException(status_code=404, detail="Favorite not found")
    return db_favorite

@router.get("/favorites/", response_model=List[schemas.Favorite])
def read_favorites(token: str, db: Session = Depends(get_db)):
    current_user = get_current_user(db, token)
    return crud.get_favorites(db=db, user_id=current_user.id)

@router.delete("/favorites/{favorite_id}")
def delete_favorite(token: str, favorite_id: int, db: Session = Depends(get_db)):
    current_user = get_current_user(db, token)
    crud.delete_favorite(user_id = current_user.id ,db=db, favorite_id=favorite_id)
    return {"message": "Favorite deleted successfully"}

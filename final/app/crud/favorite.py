from sqlalchemy.orm import Session
from fastapi import HTTPException, status

import models
import schemas


def create_favorite(user_id: int, db: Session, favorite: schemas.FavoriteCreate):
    db_favorite = models.Favorite(user_id=user_id, paper_id=favorite.paper_id)
    db.add(db_favorite)
    db.commit()
    db.refresh(db_favorite)
    return db_favorite

def get_favorite(db: Session, favorite_id: int):
    return db.query(models.Favorite).filter(models.Favorite.id == favorite_id).first()

def get_favorites(db: Session, user_id: int):
    return db.query(models.Favorite).filter(models.Favorite.user_id == user_id).all()

def delete_favorite(user_id: int, db: Session, favorite_id: int):
    db_favorite = db.query(models.Favorite).filter(models.Favorite.id == favorite_id).first()
    if not db_favorite:
        raise HTTPException(status_code=404, detail="Field not found")
    if db_favorite.user_id != user_id:
        raise HTTPException(status_code=403, detail="Do not have premission to delete")
    db.delete(db_favorite)
    db.commit()


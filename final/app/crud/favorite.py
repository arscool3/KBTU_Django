from sqlalchemy.orm import Session
import models

def add_to_favorites(db: Session, user_id: int, paper_id: int):
    favorite = models.Favorite(user_id=user_id, paper_id=paper_id)
    db.add(favorite)
    db.commit()
    db.refresh(favorite)
    return favorite

def remove_from_favorites(db: Session, user_id: int, paper_id: int):
    favorite = db.query(models.Favorite).filter(models.Favorite.user_id == user_id, models.Favorite.paper_id == paper_id).first()
    if favorite:
        db.delete(favorite)
        db.commit()
        return 'OK'
    raise HTTPException(status_code=404, detail="Favorite not found")


def get_favorites_for_user(db: Session, user_id: int):
    return db.query(models.Favorite).filter(models.Favorite.user_id == user_id).all()




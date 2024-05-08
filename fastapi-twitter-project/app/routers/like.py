from fastapi import FastAPI, status, Response, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas, utils, oauth2, database

router = APIRouter(
    prefix="/like",
    tags=['LIKE']
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def like(like: schemas.LikeCreate, db: Session = Depends(database.get_db),
         current_user: int = Depends(oauth2.get_current_user)):
    tweet = db.query(models.Tweet).filter(models.Tweet.id == like.tweet_id).first()
    if not tweet:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Tweet with ID: {like.tweet_id} does not exist")
    like_query = db.query(models.Like).filter(models.Like.tweet_id == like.tweet_id,
                                              models.Like.user_id == current_user.id)
    found_like = like_query.first()
    if like.dir == 1:
        if found_like:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail=f"user {current_user.id} has already liked a tweet {like.tweet_id}")
        new_like = models.Like(tweet_id=like.tweet_id, user_id=current_user.id)
        db.add(new_like)
        db.commit()
        return {"message": "successfully added like"}
    else:
        if not found_like:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Like does not exists")

        like_query.delete(synchronize_session=False)
        db.commit()
        return {"message": "successfully deleted like"}

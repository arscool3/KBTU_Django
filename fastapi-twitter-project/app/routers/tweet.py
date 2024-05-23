from typing import List, Optional
from sqlalchemy import func
from fastapi import FastAPI, status, Response, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas, oauth2
from ..database import get_db

router = APIRouter(
    prefix='/tweets',
    tags=['Tweets']
)


@router.get("/", response_model=List[schemas.TweetOut])
def get_tweets(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user), limit: int = 10,
               offset: int = 0, search: Optional[str] = ""):
    # print(limit)
    tweets = db.query(models.Tweet).filter(
        models.Tweet.content.contains(search)).limit(limit).offset(offset).all()
    # tweets = db.query(models.Tweet, func.count(models.Like.tweet_id).label("tweets")).join(
    #     models.Like, models.Like.tweet_id == models.Tweet.id, isouter=True).group_by(models.Tweet.id).filter(
    #     models.Tweet.content.contains(search)).limit(limit).offset(offset).all()

    return tweets


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Tweet)
def create_tweets(tweet: schemas.TweetCreate, db: Session = Depends(get_db),
                  current_user: int = Depends(oauth2.get_current_user)):
    new_tweet = models.Tweet(user=current_user, **tweet.dict())
    db.add(new_tweet)
    db.commit()
    db.refresh(new_tweet)
    return new_tweet




@router.get("/{id}", response_model=schemas.TweetOut)
def get_tweet(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # tweet = db.query(models.Tweet).filter(models.Tweet.id == id).first()

    tweet = db.query(models.Tweet).filter(models.Tweet.id == id).first()

    if not tweet:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"tweet with id {id} not found")

    # if tweet.owner_id != current_user.id:
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action!")

    return tweet


# def find_index_tweet(id):
#     for i, p in enumerate(my_tweets):
#         if p['id'] == id:
#             return i


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_tweet(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    tweet_query = db.query(models.Tweet).filter(models.Tweet.id == id)

    tweet = tweet_query.first()

    if tweet == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"tweet with id {id} was not found")

    if tweet.author_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action!")

    tweet_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", response_model=schemas.Tweet)
def update_tweet(id: int, updated_tweet: schemas.TweetCreate, db: Session = Depends(get_db),
                 current_user: int = Depends(oauth2.get_current_user)):
    tweet_query = db.query(models.Tweet).filter(models.Tweet.id == id)

    tweet = tweet_query.first()

    if tweet == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"tweet with id {id} does not exist")

    if tweet.author_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action!")

    tweet_query.update(updated_tweet.dict(), synchronize_session=False)

    db.commit()
    return tweet_query.first()

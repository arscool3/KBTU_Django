from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.schemas.review import ReviewCreate
from app.models.review import Review
from app.models.user import User
from app.dependencies.database import get_db
from app.dependencies.auth import get_current_user

router = APIRouter()


@router.post("/reviews/", status_code=status.HTTP_201_CREATED)
async def create_review(review: ReviewCreate, current_user: User = Depends(get_current_user),
                        db: Session = Depends(get_db)):
    db_review = Review(user_id=current_user.id, book_id=review.book_id, content=review.content)
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review


@router.get("/reviews/")
async def read_reviews(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    reviews = db.query(Review).offset(skip).limit(limit).all()
    return reviews


@router.get("/reviews/{review_id}")
async def read_review(review_id: int, db: Session = Depends(get_db)):
    review = db.query(Review).filter(Review.id == review_id).first()
    if not review:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Review not found")
    return review


@router.delete("/reviews/{review_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_review(review_id: int, db: Session = Depends(get_db)):
    db_review = db.query(Review).filter(Review.id == review_id).first()
    if not db_review:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Review not found")
    db.delete(db_review)
    db.commit()

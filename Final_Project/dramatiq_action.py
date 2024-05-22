# dramatiq_actions.py
import dramatiq
from sqlalchemy.orm import Session
from datetime import date, timedelta

import models


@dramatiq.actor
def borrow_book_async(db_session_str: str, book_id: int, member_id: int):
    from database import SessionLocal

    db = SessionLocal()
    try:
        book = db.query(models.Book).filter(models.Book.id == book_id).first()
        member = db.query(models.Member).filter(models.Member.id == member_id).first()

        if not book:
            raise ValueError("Book not found")

        if not member:
            raise ValueError("Member not found")

        if not book.available:
            raise ValueError("Book is not available for loan")

        loan_date = date.today()
        return_date = loan_date + timedelta(days=14)

        loan = models.Loan(book_id=book_id, member_id=member_id, loan_date=loan_date, return_date=return_date)
        db.add(loan)
        db.commit()
        db.refresh(loan)

    finally:
        db.close()

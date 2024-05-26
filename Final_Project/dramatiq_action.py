import dramatiq
from sqlalchemy.orm import Session
from database import SessionLocal
import crud

@dramatiq.actor
def borrow_book_async(db_str: str, book_id: int, member_id: int):
    db: Session = None
    try:
        db = SessionLocal()
        print("Borrowing started...")
        success = crud.borrow_book(db, book_id, member_id)
        return success
    finally:
        if db:
            db.close()

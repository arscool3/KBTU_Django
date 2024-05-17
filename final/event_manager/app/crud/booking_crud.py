# from typing import List
# from sqlalchemy.orm import Session
# from models.models import Booking as DBBooking
# from schemas.schemas import Booking, BookingCreate

# def create_booking(db: Session, booking: BookingCreate):
#     db_booking = DBBooking(**booking.dict())
#     db.add(db_booking)
#     db.commit()
#     db.refresh(db_booking)
#     return db_booking

# def get_booking(db: Session, booking_id: int):
#     return db.query(DBBooking).filter(DBBooking.id == booking_id).first()

# def get_all_bookings(db: Session) -> List[DBBooking]:
#     return db.query(DBBooking).all()

# def update_booking(db: Session, booking_id: int, booking_update: Booking):
#     db_booking = db.query(DBBooking).filter(DBBooking.id == booking_id).first()
#     if db_booking:
#         for attr, value in booking_update.dict(exclude_unset=True).items():
#             setattr(db_booking, attr, value)
#         db.commit()
#         db.refresh(db_booking)
#     return db_booking

# def delete_booking(db: Session, booking_id: int):
#     db_booking = db.query(DBBooking).filter(DBBooking.id == booking_id).first()
#     if db_booking:
#         db.delete(db_booking)
#         db.commit()
#     return db_booking

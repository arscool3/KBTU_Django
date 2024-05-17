from abc import abstractmethod
from typing import List

from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.orm import Session

import models as db
from schemas import Hotel, Room, Reservation, Review, Customer, Payment, ReturnType


class AbcRepository:

    @abstractmethod
    def __init__(self, session: Session):
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> ReturnType:
        raise NotImplementedError()

    def get_all(self) -> List[ReturnType]:
        raise NotImplementedError()


class HotelRepository(AbcRepository):
    def __init__(self, session: Session):
        self._session = session

    def get_by_id(self, id: int) -> Hotel:
        db_hotel = self._session.get(db.Hotel, id)
        if db_hotel is None:
            return None
        return Hotel.model_validate(db_hotel)

    def get_all(self) -> List[Hotel]:
        db_hotels = self._session.query(db.Hotel).all()
        return [Hotel.model_validate(hotel) for hotel in db_hotels]


class RoomRepository(AbcRepository):
    def __init__(self, session: Session):
        self._session = session

    def get_by_id(self, id: int) -> Room:
        db_room = self._session.get(db.Room, id)
        if db_room is None:
            return None
        return Room.model_validate(db_room)

    def get_all(self) -> List[Room]:
        db_rooms = self._session.query(db.Room).all()
        return [Room.model_validate(room) for room in db_rooms]



class CustomerRepository(AbcRepository):
    def __init__(self, session: Session):
        self._session = session

    def get_by_id(self, id: int) -> Customer:
        db_customer = self._session.get(db.Customer, id)
        if db_customer is None:
            return None
        return Customer.model_validate(db_customer)

    def get_all(self) -> List[Customer]:
        db_customers = self._session.query(db.Customer).all()
        return [Customer.model_validate(customer) for customer in db_customers]


class ReservationRepository(AbcRepository):
    def __init__(self, session: Session):
        self._session = session

    def get_by_id(self, id: int) -> Reservation:
        db_reservation = self._session.get(db.Reservation, id)
        if db_reservation is None:
            return None
        return Reservation.model_validate(db_reservation)

    def get_all(self) -> List[Reservation]:
        db_reservations = self._session.query(db.Reservation).all()
        return [Reservation.model_validate(reservation) for reservation in db_reservations]


class ReviewRepository(AbcRepository):
    def __init__(self, session: Session):
        self._session = session

    def get_by_id(self, id: int) -> Review:
        db_review = self._session.get(db.Review, id)
        if db_review is None:
            return None
        return Review.model_validate(db_review)

    def get_all(self) -> List[Review]:
        db_reviews = self._session.query(db.Review).all()
        return [Review.model_validate(review) for review in db_reviews]


class PaymentRepository(AbcRepository):
    def __init__(self, session: Session):
        self._session = session

    def get_by_id(self, id: int) -> Payment:
        db_payment = self._session.get(db.Payment, id)
        if db_payment is None:
            return None
        return Payment.model_validate(db_payment)

    def get_all(self) -> List[Payment]:
        db_payments = self._session.query(db.Payment).all()
        return [Payment.model_validate(payment) for payment in db_payments]
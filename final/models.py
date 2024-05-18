from datetime import datetime
from enum import Enum
from typing import Annotated

import sqlalchemy
from sqlalchemy.orm import mapped_column, Mapped, relationship

from database import Base

_id = Annotated[int, mapped_column(sqlalchemy.Integer, primary_key=True)]


class Hotel(Base):
    __tablename__ = 'hotels'

    id: Mapped[_id]
    name: Mapped[str]
    address: Mapped[str]
    stars: Mapped[int]
    rooms: Mapped['Room'] = relationship(back_populates='hotel')
    reviews: Mapped['Review'] = relationship(back_populates='hotel')


class RoomType(Enum):
    double = 'double'
    king = 'king'
    two_double = 'two double'
    suite = 'suite'


class Room(Base):
    __tablename__ = 'rooms'

    id: Mapped[_id]
    room_no: Mapped[Annotated[int, mapped_column(sqlalchemy.Integer, unique=True)]]
    type: Mapped[RoomType]
    price: Mapped[int]
    available: Mapped[Annotated[bool, mapped_column(sqlalchemy.Boolean, default=True)]]
    hotel_id: Mapped[int] = mapped_column(sqlalchemy.ForeignKey('hotels.id'))
    hotel: Mapped['Hotel'] = relationship(back_populates='rooms')
    reservation: Mapped['Reservation'] = relationship(back_populates='room')


class Customer(Base):
    __tablename__ = 'customers'

    id: Mapped[_id]
    first_name: Mapped[str]
    last_name: Mapped[str]
    phone_number: Mapped[str]
    reservation: Mapped['Reservation'] = relationship(back_populates='customer')
    reviews: Mapped['Review'] = relationship(back_populates='customer')


class Reservation(Base):
    __tablename__ = 'reservations'

    id: Mapped[_id]
    room_id: Mapped[int] = mapped_column(sqlalchemy.ForeignKey('rooms.id'))
    customer_id: Mapped[int] = mapped_column(sqlalchemy.ForeignKey('customers.id'))
    room: Mapped['Room'] = relationship(back_populates='reservation')
    customer: Mapped['Customer'] = relationship(back_populates='reservation')
    payment: Mapped['Payment'] = relationship(back_populates='reservation')


class Review(Base):
    __tablename__ = 'reviews'

    id: Mapped[_id]
    rating: Mapped[int]
    comment: Mapped[str]
    created_at: Mapped[datetime]
    hotel_id: Mapped[int] = mapped_column(sqlalchemy.ForeignKey('hotels.id'))
    hotel: Mapped['Hotel'] = relationship(back_populates='reviews')
    customer_id: Mapped[int] = mapped_column(sqlalchemy.ForeignKey('customers.id'))
    customer: Mapped['Customer'] = relationship(back_populates='reviews')


class Payment(Base):
    __tablename__ = 'payments'

    id: Mapped[_id]
    amount: Mapped[int]
    reservation_id: Mapped[int] = mapped_column(sqlalchemy.ForeignKey('reservations.id'))
    reservation: Mapped['Reservation'] = relationship(back_populates='payment')
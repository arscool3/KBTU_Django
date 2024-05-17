from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class BaseHotel(BaseModel):
    name: str
    address: str
    stars: int

    class Config:
        from_attributes = True


class CreateHotel(BaseHotel):
    pass


class Hotel(BaseHotel):
    id: int


class RoomTypeEnum(str, Enum):
    double = "double"
    king = "king"
    two_double = "two double"
    suite = "suite"


class BaseRoom(BaseModel):
    room_no: int
    type: RoomTypeEnum
    price: int
    available: bool = True

    class Config:
        from_attributes = True


class CreateRoom(BaseRoom):
    hotel_id: int


class Room(BaseRoom):
    id: int
    hotel: Hotel


class BaseCustomer(BaseModel):
    first_name: str
    last_name: str
    phone_number: str

    class Config:
        from_attributes = True


class CreateCustomer(BaseCustomer):
    pass


class Customer(BaseCustomer):
    id: int


class BaseReservation(BaseModel):
    class Config:
        from_attributes = True


class CreateReservation(BaseReservation):
    room_id: int
    customer_id: int


class Reservation(BaseReservation):
    id: int
    room: Room
    customer: Customer


class BaseReview(BaseModel):
    rating: int
    comment: str
    created_at: datetime

    class Config:
        from_attributes = True


class CreateReview(BaseReview):
    hotel_id: int
    customer_id: int


class Review(BaseReview):
    id: int
    hotel: Hotel
    customer: Customer


class BasePayment(BaseModel):
    amount: int

    class Config:
        from_attributes = True


class CreatePayment(BasePayment):
    reservation_id: int


class Payment(BasePayment):
    id: int
    reservation: Reservation


ReturnType = Hotel | Room | Customer | Reservation | Review | Payment
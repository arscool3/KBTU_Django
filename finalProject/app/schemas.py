import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    email: EmailStr
    password: str


class UserResponse(UserBase):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True


class requestdetails(BaseModel):
    email: str
    password: str


class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str


class changepassword(BaseModel):
    email: str
    old_password: str
    new_password: str


class forgotpassword(BaseModel):
    email: EmailStr


class TokenCreate(BaseModel):
    user_id: str
    access_token: str
    refresh_token: str
    status: bool
    created_date: datetime.datetime


class BusResponse(BaseModel):
    id: int
    registration_number: str
    capacity: int

    class Config:
        orm_mode = True


class BusCreate(BaseModel):
    registration_number: str
    capacity: int


class RouteCreate(BaseModel):
    origin: str
    destination: str
    stops: Optional[list[str]] = None


class RouteResponse(BaseModel):
    id: int
    origin: str
    destination: str
    stops: list[str]

    class Config:
        orm_mode = True


class ScheduleCreate(BaseModel):
    departure_datetime: datetime.datetime
    bus_id: int
    route_id: int


class ScheduleResponse(BaseModel):
    id: int
    departure_datetime: datetime.datetime
    bus_id: int
    route_id: int

    class Config:
        orm_mode = True


class SeatCreate(BaseModel):
    seat_number: int
    seat_type: str
    schedule_id: int


class SeatResponse(BaseModel):
    id: int
    seat_number: int
    seat_type: str
    schedule_id: int
    schedule: ScheduleResponse  # Include nested Schedule data

    class Config:
        orm_mode = True


class BookingCreate(BaseModel):
    user_id: int
    seat_id: int
    booking_date: datetime.datetime


class BookingResponse(BaseModel):
    id: int
    user_id: int
    seat_id: int
    booking_date: datetime.datetime
    user: UserResponse  # Include nested User data (if applicable)
    seat: SeatResponse  # Include nested Seat data

    class Config:
        orm_mode = True

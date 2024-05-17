import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    email: EmailStr
    password: str


class User(UserBase):
    id: int

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


class Route(BaseModel):
    origin: str
    destination: str
    stops: Optional[list[str]] = None  # Include stops if needed


class Schedule(BaseModel):
    departure_datetime: datetime.datetime
    bus_id: int
    route_id: int
    bus: BusCreate
    route: Route


class Seat(BaseModel):
    seat_number: int
    seat_type: str
    schedule_id: int
    schedule: Schedule  # Optional: Include nested Schedule information if desired


class Booking(BaseModel):
    user_id: int
    seat_id: int
    booking_date: datetime.datetime
    user: User  # Optional: Include nested User information if desired
    seat: Seat  # Optional: Include nested Seat information if desired

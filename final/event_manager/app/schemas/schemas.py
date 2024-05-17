from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Schema for creating a new user
class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    
class UserLogin(BaseModel):
    email: str
    password: str

# Schema for user details
class User(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        orm_mode = True

# Schema for creating a new event
class EventCreate(BaseModel):
    name: str
    description: str
    date_time: datetime
    organizer_id: int
    category_id: int

# Schema for updating an event
class EventUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    date_time: Optional[datetime] = None
    organizer_id: Optional[int] = None
    category_id: Optional[int] = None

# Schema for event details
class Event(BaseModel):
    id: int
    name: str
    description: str
    date_time: datetime
    organizer_id: int
    category_id: int

    class Config:
        orm_mode = True

# Schema for creating a new booking
class BookingCreate(BaseModel):
    user_id: int
    event_id: int

# Schema for booking details
class Booking(BaseModel):
    id: int
    user_id: int
    event_id: int

    class Config:
        orm_mode = True


class CategoryCreate(BaseModel):
    name: str

class Category(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class CategoryUpdate(BaseModel):
    name: Optional[str] = None

    class Config:
        orm_mode = True


class VenueCreate(BaseModel):
    name: str
    address: str
    city: str
    state: str
    country: str

    class Config:
        orm_mode = True

class Venue(BaseModel):
    id: int
    name: str
    address: str
    city: str
    state: str
    country: str

    class Config:
        orm_mode = True


from pydantic import BaseModel
from datetime import datetime
class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_blocked: bool

    class Config:
        orm_mode = True

class CountryCreate(BaseModel):
    name: str

class Country(BaseModel):
    id: int
    name: str
    class Config:
        orm_mode = True

class CityBase(BaseModel):
    name: str
    city_code: str
    country_id: int

class CityCreate(BaseModel):
    name: str
    city_code: str
    country_id: int

class City(CityBase):
    id: int
    class Config:
        orm_mode = True

class AirportBase(BaseModel):
    name: str

class AirportCreate(AirportBase):
    city_id: int

class Airport(AirportBase):
    id: int

    class Config:
        orm_mode = True


class PlaneBase(BaseModel):
    name: str
    capacity: int


class PlaneCreate(PlaneBase):
    pass


class PlaneUpdate(PlaneBase):
    pass


class Plane(PlaneBase):
    id: int

    class Config:
        orm_mode = True


class FlightBase(BaseModel):
    departure_airport_id: int
    destination_airport_id: int
    plane_id: int
    departure_time: datetime
    arrival_time: datetime

class FlightCreate(FlightBase):
    pass

class FlightUpdate(FlightBase):
    pass

class Flight(FlightBase):
    id: int

    class Config:
        orm_mode = True

class TicketBase(BaseModel):
    flight_id: int
    user_id: int
    # plane_id: int
    seat_number: str

class TicketCreate(TicketBase):
    pass

class Ticket(TicketBase):
    id: int
    is_reserved: bool
    class Config:
        orm_mode = True
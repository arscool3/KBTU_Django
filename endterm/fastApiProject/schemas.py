from pydantic import BaseModel, DateTime

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

class CountryBase(BaseModel):
    name: str

class CountryCreate(CountryBase):
    pass

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
    pass

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

class PlaneCreate(BaseModel):
    name: str
    capacity: str

class Plane(BaseModel):
    id: int

    class Config:
        orm_mode = True

class FlightBase(BaseModel):
    departure_airport_id: int
    destination_airport_id: int
    departure_time: DateTime
    arrival_time: DateTime

class FlightCreate(FlightBase):
    pass

class Flight(FlightBase):
    id: int

    class Config:
        orm_mode = True
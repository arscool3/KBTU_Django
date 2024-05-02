from pydantic import BaseModel

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
import datetime
import uuid

from asyncpg import types
from pydantic import BaseModel
from sqlalchemy import create_engine,String, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database import Base
import os


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_blocked = Column(Boolean, default=False)

    tickets = relationship("Ticket", back_populates="user")

class Country(Base):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)

    cities = relationship("City", back_populates="country")


class City(Base):
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    city_code = Column(String, unique=True, index=True)

    country_id = Column(Integer, ForeignKey("countries.id"))

    country = relationship("Country", back_populates="cities")
    airports = relationship("Airport", back_populates="city")


class Airport(Base):
    __tablename__ = "airports"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    city_id = Column(Integer, ForeignKey("cities.id"))

    city = relationship("City", back_populates="airports")

    departing_flights = relationship("Flight", foreign_keys="[Flight.departure_airport_id]",
                                     back_populates="departure_airport")  # Adjusted relationship
    arriving_flights = relationship("Flight", foreign_keys="[Flight.destination_airport_id]",
                                    back_populates="destination_airport")


class Plane(Base):
    __tablename__ = "planes"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    capacity = Column(Integer)

    tickets = relationship("Ticket", back_populates="plane")


class Flight(Base):
    __tablename__ = "flights"

    id = Column(Integer, primary_key=True)
    departure_airport_id = Column(Integer, ForeignKey("airports.id"))
    destination_airport_id = Column(Integer, ForeignKey("airports.id"))

    departure_time = Column(DateTime)
    arrival_time = Column(DateTime)

    departure_airport = relationship("Airport", foreign_keys=[departure_airport_id], back_populates="departing_flights")
    destination_airport = relationship("Airport", foreign_keys=[destination_airport_id], back_populates="arriving_flights")

    tickets = relationship("Ticket", back_populates="flight")


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    flight_id = Column(Integer, ForeignKey("flights.id"))
    plane_id = Column(Integer, ForeignKey("planes.id"))

    seat_number = Column(String)
    is_reserved = Column(Boolean, default=False)

    user = relationship("User", back_populates="tickets")
    flight = relationship("Flight", back_populates="tickets")
    plane = relationship("Plane", back_populates="tickets")
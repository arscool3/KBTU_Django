from click import DateTime
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    full_name = Column(String)

    # Relationships
    organized_events = relationship("Event", back_populates="organizer")
    bookings = relationship("Booking", back_populates="user")

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    date_time = Column(DateTime)
    location_id = Column(Integer, ForeignKey("locations.id"))
    organizer_id = Column(Integer, ForeignKey("users.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))

    # Relationships
    organizer = relationship("User", back_populates="organized_events")
    location = relationship("Location", back_populates="events")
    category = relationship("Category", back_populates="events")
    bookings = relationship("Booking", back_populates="event")



class Venue(Base):
    __tablename__ = "venues"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    address = Column(String)
    city = Column(String)
    state = Column(String)
    country = Column(String)

    # Relationships
    events = relationship("Event", back_populates="location")

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    # Relationships
    events = relationship("Event", back_populates="category")


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    event_id = Column(Integer, ForeignKey("events.id"))

    # Relationships
    user = relationship("User", back_populates="bookings")
    event = relationship("Event", back_populates="bookings")


class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String)
    state = Column(String)
    country = Column(String)

    # Relationships
    events = relationship("Event", back_populates="location")

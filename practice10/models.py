from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    health = Column(Integer)
    score = Column(Integer)
    weapons = relationship("Weapon", back_populates="owner")

class Weapon(Base):
    __tablename__ = "weapons"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    damage = Column(Integer)
    owner_id = Column(Integer, ForeignKey("players.id"))

    owner = relationship("Player", back_populates="weapons")

class Bot(Base):
    __tablename__ = "bots"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    health = Column(Integer)
    score = Column(Integer)

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Player(Base):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    team_id = Column(Integer, ForeignKey('teams.id'))

    team = relationship("Team", back_populates="players")

class Team(Base):
    __tablename__ = 'teams'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    players = relationship("Player", back_populates="team")
    matches = relationship("Match", back_populates="team")

class Match(Base):
    __tablename__ = 'matches'
    id = Column(Integer, primary_key=True, index=True)
    team_id = Column(Integer, ForeignKey('teams.id'))
    player_id = Column(Integer, ForeignKey('players.id'))
    date = Column(DateTime)

    team = relationship("Team", back_populates="matches")
    player = relationship("Player", back_populates="matches")

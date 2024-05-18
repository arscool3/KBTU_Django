from typing import Annotated
import sqlalchemy
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base

_id = Annotated[int, mapped_column(sqlalchemy.Integer, primary_key=True)]


class Star(Base):
    __tablename__ = 'stars'

    id: Mapped[_id]
    name: Mapped[str]
    weight: Mapped[int]
    radius: Mapped[int]
    temperature: Mapped[int]

    planet: Mapped['Planet'] = relationship(back_populates='star')


class Planet(Base):
    __tablename__ = 'planets'

    id: Mapped[_id]
    name: Mapped[str]
    weight: Mapped[int]
    radius: Mapped[int]
    habitable: Mapped[bool]

    star_id: Mapped[int] = mapped_column(sqlalchemy.ForeignKey('stars.id'))
    # resident_id = Mapped['Resident'] = relationship(back_populates='planet')

    star: Mapped[Star] = relationship("Star", back_populates="planet")
    satellite: Mapped['Satellite'] = relationship(back_populates='planet')
    # resident = Mapped['Resident'] = relationship(back_populates='planets')


class Satellite(Base):
    __tablename__ = 'satellites'

    id: Mapped[_id]
    name: Mapped[str]
    weight: Mapped[int]
    radius: Mapped[int]
    habitable: Mapped[bool]

    planet_id: Mapped[int] = mapped_column(sqlalchemy.ForeignKey('planets.id'))

    planet: Mapped[Planet] = relationship("Planet", back_populates="satellite")
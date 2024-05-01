import sqlalchemy as sa

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, Mapped, mapped_column, relationship
from sqlalchemy.ext.declarative import declarative_base

url = 'postgresql://postgres:postgres@localhost/postgres'
engine = create_engine(url)
session = Session(engine)

Base = declarative_base()


class Person(Base):
    __tablename__ = 'people'
    id: Mapped[int] = mapped_column(sa.INTEGER, primary_key=True)
    name: Mapped[str]
    is_driver: Mapped[bool] = mapped_column(sa.Boolean, default=False)
    car_id: Mapped[int] = mapped_column(sa.ForeignKey("cars.id"))
    car: Mapped['Car'] = relationship(back_populates='people')


class Car(Base):
    __tablename__ = 'cars'
    id: Mapped[int] = mapped_column(sa.INTEGER, primary_key=True)
    brand: Mapped[str]
    model: Mapped[str]
    year: Mapped[int]
    people: Mapped[list[Person]] = relationship(back_populates='car')

# Car -> Person (One to Many)


# Engine and Session

# Arslan Bank Account -> Daulet Bank Account

# Arslan -> Daulet 1000 tng

# 2 sql queries

# Arslan -1000 tng

# Сбой

# Daulet +1000 tng


# Atomicity Transaction

# Begin session / transaction
# Arslan -1000
# Сбой
# Daulet +1000
# End session / transaction
# Commit

import sqlalchemy as sa

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, Mapped, mapped_column, relationship
from sqlalchemy.ext.declarative import declarative_base

url = 'postgresql://postgres:postgres@localhost/postgres'
engine = create_engine(url)
session = Session(engine)

Base = declarative_base()


class Chocolate(Base):
    __tablename__ = 'chocolates'
    id: Mapped[int] = mapped_column(sa.INTEGER, primary_key=True)
    name: Mapped[str]
    is_sweet: Mapped[bool] = mapped_column(sa.Boolean, default=False)
    box_id: Mapped[int] = mapped_column(sa.ForeignKey("boxes.id"))
    box: Mapped['Box'] = relationship(back_populates='chocolate')


class Box(Base):
    __tablename__ = 'boxes'
    id: Mapped[int] = mapped_column(sa.INTEGER, primary_key=True)
    brand: Mapped[str]
    volume: Mapped[int]
    people: Mapped[list[Chocolate]] = relationship(back_populates='box')



import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, Mapped, mapped_column, relationship
from sqlalchemy.ext.declarative import declarative_base

from config import *

url = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
engine = create_engine(url)
session = Session(engine)

Base = declarative_base()


class Company(Base):
    __tablename__ = 'company_table'
    id: Mapped[int] = mapped_column(sa.INTEGER, primary_key=True)
    name: Mapped[str]
    phone_number: Mapped[str]
    vacancy: Mapped[list['Vacancy']] = relationship(back_populates='vacancy')


class Vacancy(Base):
    __tablename__ = 'vacancy_table'
    id: Mapped[int] = mapped_column(sa.INTEGER, primary_key=True)
    name: Mapped[str]
    description: Mapped[str]
    category_id: Mapped[int] = mapped_column(sa.ForeignKey("category_table.id"))
    category: Mapped['Category'] = relationship(back_populates='category')
    campany_id: Mapped[int] = mapped_column(sa.ForeignKey("company_table.id"))
    company: Mapped['Company'] = relationship(back_populates='company')


class Category(Base):
    __tablename__ = 'category_table'
    id: Mapped[int] = mapped_column(sa.INTEGER, primary_key=True)
    name: Mapped[str]
    vacancy: Mapped[list['Vacancy']] = relationship(back_populates='vacancy')
import sqlalchemy as sa

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base

url = 'postgresql://postgres:postgres@localhost/postgres'
engine = create_engine(url)
session = Session(engine)

Base = declarative_base()

class Ingredient(Base):
    id: Mapped[int] = mapped_column(sa.INTEGER, primary_key=True)
    title: Mapped[str]
    description: Mapped[str]
    __tablename__= 'ingredients'

class Comment(Base):
    id: Mapped[int] = mapped_column(sa.INTEGER, primary_key=True)
    title: Mapped[str]
    description: Mapped[str]
    __tablename__= 'comments' 

class Recipe(Base):
    __tablename__= 'recipe'
    id: Mapped[int] = mapped_column(sa.INTEGER, primary_key=True)
    title: Mapped[str]
    description: Mapped[str]

class Category(Base):
    id: Mapped[int] = mapped_column(sa.INTEGER, primary_key=True)
    __tablename__= 'categories' 
    title: Mapped[str]
    description: Mapped[str]

class Article(Base):
    id: Mapped[int] = mapped_column(sa.INTEGER, primary_key=True)
    __tablename__ ='articles'
    title: Mapped[str]
    description: Mapped[str]

class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(sa.INTEGER, primary_key=True)
    username: Mapped[str]

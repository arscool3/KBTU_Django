import sqlalchemy as sa

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, Mapped, mapped_column, relationship
from sqlalchemy.ext.declarative import declarative_base

url = 'postgresql://postgres:postgres@localhost/postgres'
engine = create_engine(url)
session = Session(engine)

Base = declarative_base()

#class Basic_model(Base):
    

class Ingredient(Base):
    id: Mapped[int] = mapped_column(sa.INTEGER, primary_key=True)
    description: Mapped[str]
    __tablename__= 'ingredients'

class Comment(Base):
    id: Mapped[int] = mapped_column(sa.INTEGER, primary_key=True)
    description: Mapped[str]
    __tablename__= 'comments' 

class Recipe(Base):
    __tablename__= 'recipe'
    id: Mapped[int] = mapped_column(sa.INTEGER, primary_key=True)
    user_id: Mapped[int] = mapped_column(sa.ForeignKey("users.id"))
    comments: Mapped[list[Comment]] = relationship(back_populates='recipe')
    title: Mapped[str]
    description: Mapped[str]
    #ingredients: Mapped[list[Ingredient]] = relationship(back_populates='recipe')

class Category(Base):
    id: Mapped[int] = mapped_column(sa.INTEGER, primary_key=True)
    __tablename__= 'categories' 
    title: Mapped[str]
    description: Mapped[str]

class Article(Base):
    id: Mapped[int] = mapped_column(sa.INTEGER, primary_key=True)
    __tablename__ ='articles'
    user_id: Mapped[int] = mapped_column(sa.ForeignKey("user.id"))
    title: Mapped[str]
    description: Mapped[str]

class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(sa.INTEGER, primary_key=True)
    username: Mapped[str]
    recipes: Mapped[list[Recipe]] = relationship(back_populates='user')
    articles: Mapped[list[Article]] = relationship(back_populates='user')
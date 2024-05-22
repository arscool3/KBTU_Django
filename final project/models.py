import bcrypt
import sqlalchemy as sa
from sqlalchemy import create_engine, Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, Session
from sqlalchemy.ext.declarative import declarative_base

url = 'postgresql://postgres:postgres@localhost/postgres'
engine = create_engine(url)
session = Session(engine)
Base = declarative_base()


class Ingredient(Base):
    __tablename__ = 'ingredients'
    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String)
    description = sa.Column(sa.String)
    recipes = relationship("Recipe", secondary='recipe_category_association', back_populates="ingredients")

class Comment(Base):
    __tablename__ = 'comments'
    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String)
    description = sa.Column(sa.String)
    article_id = sa.Column(sa.Integer, sa.ForeignKey('articles.id'))
    article = relationship("Article", back_populates="comments")
    

class Recipe(Base):
    __tablename__ = 'recipes'
    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String)
    description = sa.Column(sa.String)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))
    user = relationship("User", back_populates="recipes")

class Category(Base):
    __tablename__ = 'categories'
    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String)
    description = sa.Column(sa.String)
    recipes = relationship("Recipe", secondary='recipe_category_association', back_populates="categories")

class Article(Base):
    __tablename__ = 'articles'
    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String)
    description = sa.Column(sa.String)
    comments = relationship("Comment", back_populates="article")
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))
    user = relationship("User", back_populates="articles")

class User(Base):
    __tablename__ = 'users'
    id = sa.Column(sa.Integer, primary_key=True)
    username = sa.Column(sa.String)
    recipes = relationship("Recipe", back_populates="user")
    articles= relationship("Article",back_populates="user")

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()
def verify_password(plain_password: str, hashed_password: str):
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
import sqlalchemy as sa

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, Mapped, mapped_column, relationship
from sqlalchemy.ext.declarative import declarative_base

url = 'postgresql://postgres:postgres@localhost/postgres'
engine = create_engine(url)
session = Session(engine)

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(sa.INTEGER, primary_key=True)
    name: Mapped[str]
    email: Mapped[str]
    is_active: Mapped[bool] = mapped_column(sa.Boolean, default=False)


class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(sa.INTEGER, primary_key=True)
    title: Mapped[str]
    content: Mapped[str]
    author_id: Mapped[int] = mapped_column(sa.ForeignKey("users.id"))
    author: Mapped['User'] = relationship(back_populates="posts")
    comments: Mapped[list['Comment']] = relationship(back_populates="post")


class Comment(Base):
    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(sa.INTEGER, primary_key=True)
    content: Mapped[str]
    post_id: Mapped[int] = mapped_column(sa.ForeignKey("posts.id"))
    post: Mapped['Post'] = relationship(back_populates="comments")

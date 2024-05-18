from sqlalchemy import Boolean, String, Column, Integer, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from db import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String, unique=True, index=True)
    hashed_password = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=False)

    posts = relationship('Post', back_populates='user')
    comments = relationship('Comment', back_populates='user')


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', back_populates='posts')
    comments = relationship('Comment', back_populates='post')


class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))

    user = relationship('User', back_populates='comments')
    post = relationship('Post', back_populates='comments')


class Likes(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))


class Profile(Base):
    __tablename__ = 'profiles'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))


class Stories(Base):
    __tablename__ = 'stories'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    content = Column(String)
    date = Column(DateTime)

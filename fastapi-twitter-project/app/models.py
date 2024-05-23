from datetime import date
from typing import Annotated, List

import sqlalchemy
from sqlalchemy import func, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .database import Base

_id = Annotated[int, mapped_column(sqlalchemy.Integer, primary_key=True)]
_created_at: Mapped[date] = mapped_column(sqlalchemy.DATE, default=func.now())


class Tweet(Base):
    __tablename__ = 'tweets'

    id: Mapped[_id]
    content: Mapped[str]
    created_at: Mapped[date] = mapped_column(default=date.today)

    author_id: Mapped[int] = mapped_column(sqlalchemy.ForeignKey('users.id'))
    user: Mapped['User'] = relationship(back_populates='tweets')
    likes: Mapped[List['Like']] = relationship(back_populates='tweet')
    retweets: Mapped['Retweet'] = relationship(back_populates='original_tweet')

    comments: Mapped[List['Comment']] = relationship(back_populates='tweet')


class User(Base):
    __tablename__ = 'users'

    id: Mapped[_id]
    username: Mapped[str]
    email: Mapped[str]
    password: Mapped[str]
    created_at: Mapped[date] = mapped_column(default=date.today)

    followers_count: Mapped[int] = mapped_column(default=0)
    following_count: Mapped[int] = mapped_column(default=0)
    tweets: Mapped[List[Tweet]] = relationship(back_populates='user')

    followers: Mapped[List['Follow']] = relationship('Follow', foreign_keys='Follow.followed_user_id', back_populates='followed')
    following: Mapped[List['Follow']] = relationship('Follow', foreign_keys='Follow.follower_id', back_populates='follower')
    likes: Mapped[List['Like']] = relationship()
    retweets: Mapped[List['Retweet']] = relationship()
    comments: Mapped[List['Comment']] = relationship()


class Follow(Base):
    __tablename__ = 'follows'
    id: Mapped[_id]

    follower_id: Mapped[int] = mapped_column(sqlalchemy.ForeignKey('users.id'), primary_key=True)
    followed_user_id: Mapped[int] = mapped_column(sqlalchemy.ForeignKey('users.id'), primary_key=True)

    follower: Mapped['User'] = relationship('User', foreign_keys=[follower_id] ,back_populates='followers')
    followed: Mapped['User'] = relationship('User', foreign_keys=[followed_user_id], back_populates='following')
    created_at: Mapped[date] = mapped_column(default=date.today)


class Like(Base):
    __tablename__ = 'likes'


    user_id: Mapped[int] = mapped_column(sqlalchemy.ForeignKey('users.id'), primary_key=True)
    tweet_id: Mapped[int] = mapped_column(sqlalchemy.ForeignKey('tweets.id'), primary_key=True)

    user: Mapped['User'] = relationship(back_populates='likes')
    tweet: Mapped['Tweet'] = relationship(back_populates='likes')
    created_at: Mapped[date] = mapped_column(default=date.today)


class Retweet(Base):
    __tablename__ = 'retweets'

    id: Mapped[_id]

    user_id: Mapped[int] = mapped_column(sqlalchemy.ForeignKey('users.id'), primary_key=True)
    original_tweet_id: Mapped[int] = mapped_column(sqlalchemy.ForeignKey('tweets.id'), primary_key=True)

    user: Mapped['User'] = relationship(back_populates='retweets')
    original_tweet: Mapped['Tweet'] = relationship(back_populates='retweets')
    created_at: Mapped[date] = mapped_column(default=date.today)


class Comment(Base):
    __tablename__ = 'comments'

    id: Mapped[_id]

    content: Mapped[str]
    created_at: Mapped[date] = mapped_column(default=date.today)

    user_id: Mapped[int] = mapped_column(sqlalchemy.ForeignKey('users.id'))
    tweet_id: Mapped[int] = mapped_column(sqlalchemy.ForeignKey('tweets.id'))
    user: Mapped[User] = relationship(back_populates='comments')
    tweet: Mapped[Tweet] = relationship(back_populates='comments')

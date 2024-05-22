from sqlalchemy import Column, Date, DateTime, Integer, String, Enum, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship

from ..database import Base
from .enums import Gender
from ..post.models import post_likes, Post


class Follow(Base):
    __tablename__ = "follows"

    follower_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    following_id = Column(Integer, ForeignKey("users.id"), primary_key=True)

    follower = relationship(
        "User", foreign_keys=[follower_id], back_populates="followers"
    )

    following = relationship(
        "User", foreign_keys=[following_id], back_populates="following"
    )


class User(Base):
    __tablename__ = "users"

    # basic details
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    name = Column(String)
    hashed_password = Column(String, nullable=False)
    created_dt = Column(DateTime, default=datetime.utcnow())

    # profile
    dob = Column(Date)
    gender = Column(Enum(Gender))
    profile_pic = Column(String)  # link to our dp
    bio = Column(String)
    location = Column(String)

    posts = relationship(Post, back_populates="author")

    liked_posts = relationship(
        Post, secondary=post_likes, back_populates="liked_by_users"
    )

    followers = relationship(
        Follow, foreign_keys=[Follow.following_id], back_populates="following"
    )
    following = relationship(
        Follow, foreign_keys=[Follow.follower_id], back_populates="follower"
    )

    followers_count = Column(Integer, default=0)
    following_count = Column(Integer, default=0)
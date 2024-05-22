from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.models.base import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    videos = relationship("Video", back_populates="user")
    comments = relationship("Comment", back_populates="user")
    streams = relationship("Stream", back_populates="user")
    subscriptions = relationship("Subscription", back_populates="user")

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base
from app.models.user import User
from app.models.stream import Stream

class Subscription(Base):
    __tablename__ = 'subscriptions'
    
    id = Column(Integer, primary_key=True, index=True)
    
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="subscriptions")
    
    stream_id = Column(Integer, ForeignKey('streams.id'))
    stream = relationship("Stream", back_populates="subscriptions")

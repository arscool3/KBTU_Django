from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base
from app.models.user import User

class Stream(Base):
    __tablename__ = 'streams'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="streams")
    subscriptions = relationship("Subscription", back_populates="stream")

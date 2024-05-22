from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base
from app.models.user import User
from app.models.video import Video

class Comment(Base):
    __tablename__ = 'comments'
    
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)

    user_id = Column(Integer, ForeignKey('users.id'))
    video_id = Column(Integer, ForeignKey('videos.id'))
    
    user = relationship("User", back_populates="comments")
    video = relationship("Video", back_populates="comments")

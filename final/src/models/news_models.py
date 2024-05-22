from database import Base
from enum import Enum
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.orm import relationship


class News(Base):
    __tablename__ = 'news'

    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String, nullable=False)
    text = Column(String, nullable=False)
    date = Column(Date, nullable=False)

    author = relationship("User", uselist=False, back_populates="news")

    
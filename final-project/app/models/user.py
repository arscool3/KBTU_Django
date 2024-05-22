from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.dependencies.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    reviews = relationship("Review", back_populates="user")

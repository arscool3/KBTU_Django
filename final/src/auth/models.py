from database import Base
from enum import Enum
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.orm import relationship


class RoleEnum(Enum):
    STUDENT = "STUDENT"
    INSTRUCTOR = "INSTRUCTOR"


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(200), nullable=False)
    role = Column(ENUM(RoleEnum), nullable=False)

    instructor = relationship("Instructor", uselist=False, back_populates="user")
    student = relationship("Student", uselist=False, backref="user")

    
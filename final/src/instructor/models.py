from database import Base
from sqlalchemy import Column, Integer, ForeignKey
from auth.models import User
from sqlalchemy.orm import relationship


class Instructor(Base):
    __tablename__ = 'instructors'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))

    courses = relationship("Course", backref="tutor")

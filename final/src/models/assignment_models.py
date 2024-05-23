from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Assignment(Base):
    __tablename__ = 'assignments'

    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    course_id = Column(Integer, ForeignKey('courses.id'))
    max_points = Column(Integer, nullable=True)

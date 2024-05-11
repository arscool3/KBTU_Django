from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    instructor_id = Column(Integer, ForeignKey('instructors.id'))

    instructor = relationship("Instructor", backref="course_list", uselist=False)
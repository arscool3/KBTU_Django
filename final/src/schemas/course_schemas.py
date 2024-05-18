from enum import Enum
from pydantic import BaseModel


class CourseBase(BaseModel):
    name: str
    instructor_id: int

class CourseCreate(CourseBase):
   pass

class Course(BaseModel):
    id: int

from enum import Enum
from pydantic import BaseModel

class CourseCreate(BaseModel):
    name: str
    instructor_id: int

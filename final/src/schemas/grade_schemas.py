from enum import Enum
from pydantic import BaseModel


class GradeBase(BaseModel):
    name: str
    assignment_id: int
    student_id: int

class GradeCreate(GradeBase):
   pass

class Grade(GradeBase):
    id: int

from enum import Enum
from pydantic import BaseModel


class AssignmentBase(BaseModel):
    name: str
    course_id: int

class AssignmentCreate(AssignmentBase):
    pass

class Assignment(BaseModel):
    id: int



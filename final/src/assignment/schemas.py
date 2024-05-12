from enum import Enum
from pydantic import BaseModel

class AssignmentCreate(BaseModel):
    name: str
    course_id: int

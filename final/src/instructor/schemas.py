from pydantic import BaseModel, Field
from auth.models import User


class InstructorBase(BaseModel):
    user_id: int = Field(default=None, foreign_key="users.id")

class InstructorCreate(InstructorBase):
    pass

class Instructor(InstructorBase):
    id: int
    user: User

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

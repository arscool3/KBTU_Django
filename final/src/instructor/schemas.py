from pydantic import BaseModel, Field


class InstructorCreate(BaseModel):
    user_id: int = Field(default=None, foreign_key="users.id")

from pydantic import BaseModel, Field


class StudentCreate(BaseModel):
    user_id: int = Field(default=None, foreign_key="users.id")

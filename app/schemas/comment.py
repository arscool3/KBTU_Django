from pydantic import BaseModel

class CommentBase(BaseModel):
    content: str
    user_id: int
    video_id: int

class CommentCreate(CommentBase):
    pass

class Comment(CommentBase):
    id: int

    class Config:
        orm_mode = True
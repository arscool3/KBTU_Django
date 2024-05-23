from pydantic import BaseModel
from typing import List, Optional

class VideoBase(BaseModel):
    title: str
    description: str
    url: str

class VideoCreate(VideoBase):
    pass

class Video(VideoBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True

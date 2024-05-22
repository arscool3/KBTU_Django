from pydantic import BaseModel


class VideoBase(BaseModel):
    title: str
    description: str
    content: bytes

class VideoCreate(VideoBase):
    pass

class Video(VideoBase):
    id: int

    class Config:
        orm_mode = True
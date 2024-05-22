from pydantic import BaseModel

class StreamBase(BaseModel):
    title: str
    description: str

class StreamCreate(StreamBase):
    pass

class Stream(StreamBase):
    id: int

    class Config:
        orm_mode = True
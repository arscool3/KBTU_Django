from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str
    is_active: bool

    class Config:
        from_attributes = True


class Comment(BaseModel):
    content: str

    class Config:
        from_attributes = True


class Post(BaseModel):
    title: str
    content: str
    author: User
    comments: list[Comment]

    class Config:
        from_attributes = True

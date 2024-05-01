from pydantic import BaseModel


class UserSchema(BaseModel):
    username: str
    email: str


class PostSchema(BaseModel):
    title: str
    content: str
    author_id: int


class CommentSchema(BaseModel):
    text: str
    post_id: int

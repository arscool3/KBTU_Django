from pydantic import BaseModel
from typing import List, Optional, ForwardRef


class UserBase(BaseModel):
    username: str
    email: str

class PostBase(BaseModel):
    title: str
    content: str

class CommentBase(BaseModel):
    content: str

class PostCreate(PostBase):
    user_id: int

class UserCreate(UserBase):
    pass

class CommentCreate(CommentBase):
    user_id: int
    post_id: int

UserDisplay = ForwardRef('UserDisplay')

class PostDisplay(PostBase):
    id: int
    author: 'UserDisplay' 

class UserDisplay(UserBase):
    id: int
    posts: List[PostDisplay] = []

class CommentDisplay(CommentBase):
    id: int
    commenter: 'UserDisplay'  
    post: PostBase

PostDisplay.update_forward_refs()
UserDisplay.update_forward_refs()
CommentDisplay.update_forward_refs()

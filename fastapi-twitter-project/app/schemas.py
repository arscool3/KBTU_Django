from pydantic import EmailStr, BaseModel
from datetime import datetime
from typing import Optional, List
from pydantic.types import conint


class TweetBase(BaseModel):
    content: str


class TweetCreate(TweetBase):
    pass


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True


class Tweet(TweetBase):
    id: int
    created_at: datetime
    user: UserOut

    class Config:
        orm_mode = True


class TweetOut(BaseModel):
    content: str
    likes: List['Like']
    user: UserOut

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None


class Like(BaseModel):
    id: int
    tweet: Tweet
    user: UserOut


class LikeCreate(BaseModel):
    tweet_id: int
    dir: conint(le=1)

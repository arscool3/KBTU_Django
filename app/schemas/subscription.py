from pydantic import BaseModel

class SubscriptionBase(BaseModel):
    user_id: int
    stream_id: int

class SubscriptionCreate(SubscriptionBase):
    pass

class Subscription(SubscriptionBase):
    id: int

    class Config:
        orm_mode = True
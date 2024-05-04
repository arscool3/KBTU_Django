from pydantic import BaseModel

class PlayerBase(BaseModel):
    username: str
    health: int = 100
    score: int = 0

class PlayerCreate(PlayerBase):
    pass

class Player(PlayerBase):
    id: int

    class Config:
        orm_mode = True

class WeaponBase(BaseModel):
    name: str
    damage: int

class WeaponCreate(WeaponBase):
    pass

class Weapon(WeaponBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class BotBase(BaseModel):
    name: str
    health: int = 100
    score: int = 0

class BotCreate(BotBase):
    pass

class Bot(BotBase):
    id: int

    class Config:
        orm_mode = True

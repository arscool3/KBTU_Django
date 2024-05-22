from pydantic import BaseModel


class Chocolate(BaseModel):
    name: str
    is_sweet: bool

    class Config:
        from_attributes  = True

class Biscuit(BaseModel):
    name: str
    class Config:
        from_attributes = True


class Box(BaseModel):
    brand: str
   
    volume: int
    chocolates: list[Chocolate]
    biscuits: list[Biscuit]

    class Config:
        from_attributes = True


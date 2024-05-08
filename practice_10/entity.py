from pydantic import BaseModel


class Chocolate(BaseModel):
    name: str
    is_sweet: bool

    class Config:
        from_attributes  = True


class Box(BaseModel):
    brand: str
   
    volume: int
    chocolates: list[Chocolate]

    class Config:
        from_attributes = True


# class PersonWithCarId(Chocolate):
#     car_id: int
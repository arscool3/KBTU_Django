from pydantic import BaseModel


class Person(BaseModel):
    name: str
    is_driver: bool

    class Config:
        from_attributes  = True


class Car(BaseModel):
    brand: str
    model: str
    year: int
    people: list[Person]

    class Config:
        from_attributes = True


class PersonWithCarId(Person):
    car_id: int

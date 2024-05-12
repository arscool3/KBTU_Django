from pydantic import BaseModel


class Vacancy(BaseModel):
    name: str
    description: str

    class Config:
        from_attributes = True


class Company(BaseModel):
    name: str
    phone_number: str
    vacancy: list[Vacancy]

    class Config:
        from_attributes = True


class Category(BaseModel):
    name: str
    vacancy: list[Vacancy]

    class Config:
        from_attributes = True


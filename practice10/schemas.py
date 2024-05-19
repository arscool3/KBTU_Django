from pydantic import BaseModel
from typing import List, Optional


class EmployerBase(BaseModel):
    name: str


class EmployerCreate(EmployerBase):
    pass


class Employer(EmployerBase):
    id: int

    class Config:
        from_attributes = True


class EmployeeBase(BaseModel):
    name: str
    employer_id: int


class EmployeeCreate(EmployeeBase):
    pass


class Employee(EmployeeBase):
    id: int
    employer: Employer

    class Config:
        from_attributes = True


class JobBase(BaseModel):
    title: str
    description: str
    employer_id: int


class JobCreate(JobBase):
    pass


class Job(JobBase):
    id: int
    employer: Employer

    class Config:
        from_attributes = True

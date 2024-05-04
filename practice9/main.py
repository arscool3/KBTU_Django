from __future__ import annotations

from typing import Annotated

import punq
from fastapi import FastAPI, Depends
from pydantic import BaseModel

app = FastAPI()

candidates = []
recruiters = []
employees = []


class User(BaseModel):
    name: str
    age: int


class Candidate(User):
    pass


class Recruiter(User):
    pass


class Employee(User):
    pass


class UserSubLayer:
    def __init__(self, log_message: str):
        self.log_message = log_message

    def add_user(self, user: Candidate | Recruiter):
        print(self.log_message)
        candidates.append(user) if isinstance(user, Candidate) else recruiters.append(user)


class UserMainLayer:
    def __init__(self, repo: UserSubLayer):
        self.repo = repo

    def add_user(self, user: Candidate | Recruiter):
        print("SOME LOGGING")
        self.repo.add_user(user)
        print("END LOGGING")

        return "User was added"

    def add_candidate(self, candidate: Candidate) -> str:
        return self.add_user(candidate)

    def add_recruiter(self, recruiter: Recruiter) -> str:
        return self.add_user(recruiter)


def get_container() -> punq.Container:
    container = punq.Container()
    container.register(UserSubLayer, instance=UserSubLayer(log_message='I AM INSIDE SUB LAYER'))
    container.register(UserMainLayer)
    return container


def add_employees(employee: Employee) -> str:
    employees.append(employee)
    return "Employee added"


@app.post("/candidates")
def add_candidate(
        candidate: Annotated[str, Depends(get_container().resolve(UserMainLayer).add_candidate)]
) -> str:
    return candidate


@app.post("/recruiters")
def add_recruiter(
        recruiter: Annotated[str, Depends(get_container().resolve(UserMainLayer).add_recruiter)]
) -> str:
    return recruiter


@app.post("/employee")
async def add_employee(employee: Annotated[Employee, Depends(add_employees)]):
    return employee


@app.get("/employees")
async def get_employees() -> list[Employee]:
    return employees

from typing import Annotated

import punq
from fastapi import FastAPI, Depends
from pydantic import BaseModel

app = FastAPI()

students = []
teachers = []
employees = []


class User(BaseModel):
    name: str
    age: int


class Student(User):
    pass


class Teacher(User):
   pass


class Employee(User):
    pass


class UserSubLayer:
    def __init__(self, log_message: str):
        self.log_message = log_message

    def add_user(self, user: Student | Teacher):
        print(self.log_message)
        students.append(user) if isinstance(user, Student) else teachers.append(user)


class UserMainLayer:
    def __init__(self, repo: UserSubLayer):
        self.repo = repo

    def add_user(self, user: Student | Teacher):
        print("SOME LOGGING")
        self.repo.add_user(user)
        print("END LOGGING")

        return "user was added"

    def add_student(self, student: Student) -> str:
        return self.add_user(student)

    def add_teacher(self, teacher: Teacher) -> str:
        return self.add_user(teacher)


def get_container() -> punq.Container:
    container = punq.Container()
    container.register(UserSubLayer, instance=UserSubLayer(log_message='I AM INSIDE SUB LAYER'))
    container.register(UserMainLayer)
    return container


def add_employees(employee: Employee) -> str:
    employees.append(employee)
    return "Employee added"


@app.post("/students")
def add_book(
        student: Annotated[str, Depends(get_container().resolve(UserMainLayer).add_student)]
) -> str:
    return student


@app.post("/teachers")
def add_teacher(
        teacher: Annotated[str, Depends(get_container().resolve(UserMainLayer).add_teacher)]
) -> str:
    return teacher


@app.post("/employee")
async def add_employee(employee: Annotated[Employee, Depends(add_employees)]):
    return employee


@app.get("/employees")
async def get_employees() -> list[Employee]:
    return employees
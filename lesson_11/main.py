import random
import time
from datetime import datetime, timedelta
from http import HTTPStatus
from http.client import HTTPResponse
from typing import Annotated, Optional

from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel

# x: int = get()
# x: Annotated[int, get()]
#
# def test(x: Annotated[int, get()]):
#     print(x)


app = FastAPI()


def main():
    print('started')
    return hello()


def hello():
    return f"Hello {name()}"


def name():
    return f"Arslan {job()}"


def job():
    return ", you are SWE"


class Test(BaseModel):
    name: str
    age: int
    job: str


def gov():
    time.sleep(random.randint(1, 8))


def func(test: Test) -> Test:
    started = datetime.now()
    gov()
    ended = datetime.now()
    if ended - started > timedelta(seconds=2):
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND)

    return test


@app.post("/")
def test_logic(func_di: Annotated[Test, Depends(func)]):
    d = func_di
    return f"your job is {d.job}"


@app.post("/hello")
def test(func_di: Annotated[Test, Depends(func)]):
    d = func_di
    return f"your name is {d.name}"


class Film(BaseModel):
    id: int
    genre: str
    name: str


films = {
    1: Film(id=1, genre="noir", name="psycho"),
    2: Film(id=2, genre="detective", name="Sherlock")
}


class FilmFuncClass:
    def __init__(self, arg):
        self.arg = arg

    def di(self, film: Film) -> Film | str:
        if self.arg == 'test':
            return "test logic"
        print(film)
        return film


film_func_instance = FilmFuncClass(arg='not test')


@app.post("/test_film")
def test(di: Annotated[Film | str, Depends(film_func_instance.di)]):
    return di


def child_dependency(arg: int) -> int:
    return arg


def main_dependency(
        sub_dependency: Annotated[int, Depends(child_dependency)],
        arg_new: int
) -> int:
    return arg_new


def main_depedency_2(
    sub_dependency: Annotated[int, Depends(child_dependency)],
    arg_old: int
) -> int:
    return arg_old


@app.get("/test_sub_dependency")
def test_sub_dependency(di: Annotated[int, Depends(main_dependency)]):
    return di


@app.get("/test_sub_dependency_2")
def test_sub_dependency_2(di: Annotated[int, Depends(main_depedency_2)]):
    return di


# 30 minutes
# dependency injection 3 di1 -> di2
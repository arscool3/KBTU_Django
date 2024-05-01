from contextlib import contextmanager
from typing import Optional, Annotated

from sqlalchemy import select
from fastapi import FastAPI, HTTPException, Depends

from entity import Car, Person, PersonWithCarId
import models as db

app = FastAPI()


@contextmanager
def get_db():
    try:
        session = db.session
        yield session
        session.commit()
        session.close()
    except Exception:
        print('some exception')


@app.get("/car")
def car(id: int) -> Car:
    with get_db() as session:
        car = session.get(db.Car, id)
        if car is None:
            raise HTTPException(status_code=404)
        return Car.model_validate(car)


@app.get("/cars")
def cars() -> list[Car]:
    with get_db() as session:
        db_cars = session.execute(select(db.Car)).scalars().all()
        cars = []
        for db_car in db_cars:
            cars.append(Car.model_validate(db_car))
        return cars


class AddDependency:

    @staticmethod
    def _add_model(db_model: type[db.Car] | type[db.Person], pydantic_model: Car | Person) -> None:
        with get_db() as session:
            session.add(db_model(**pydantic_model.model_dump()))

    @classmethod
    def add_car(cls, car: Car) -> str:
        cls._add_model(db.Car, car)
        return "car was added"

    @classmethod
    def add_person(cls, person: PersonWithCarId) -> str:
        cls._add_model(db.Person, person)
        return "person was added"


@app.post("/car")
def add_car(car_di: Annotated[str, Depends(AddDependency.add_car)]) -> str:
    return car_di


@app.post("/person")
def add_person(person_di: Annotated[str, Depends(AddDependency.add_person)]) -> str:
    return person_di

# install docker
# docker run --name postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 postgres

# DBeaver
# pip install sqlalchemy
# pip install alembic
# pip install psycopg2-binary

# alembic revision -m "initial" --autogenerate
# alembic upgrade 302e22e47ab3

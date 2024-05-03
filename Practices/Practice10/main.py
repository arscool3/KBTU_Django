from __future__ import annotations

from typing import Annotated

from fastapi import FastAPI, Depends
from contextlib import contextmanager

from sqlalchemy import select

import models as db
from entity import *

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


@app.get("/vacancies")
def vacancies() -> list[Vacancy]:
    with get_db() as session:
        db_vacancies = session.execute(select(db.Vacancy)).scalars().all()
        vacancies = []
        for db_vacancy in db_vacancies:
            vacancies.append(Vacancy.model_validate(db_vacancy))
        return vacancies

@app.get("/companies")
def comps() -> list[Company]:
    with get_db() as session:
        db_comps = session.execute(select(db.Company)).scalars().all()
        comps = []
        for db_c in db_comps:
            comps.append(Company.model_validate(db_c))
        return comps


@app.get("/Category")
def cats() -> list[Category]:
    with get_db() as session:
        db_cats = session.execute(select(db.Category)).scalars().all()
        cats = []
        for db_c in db_cats:
            cats.append(Category.model_validate(db_c))
        return cats



class AddDependency:

    @staticmethod
    def _add_model(db_model: type[db.Vacancy] | type[db.Company] | type[db.Category], pydantic_model: Vacancy | Company | Category) -> None:
        with get_db() as session:
            session.add(db_model(**pydantic_model.model_dump()))

    @classmethod
    def add_vac(cls, v: Vacancy) -> str:
        cls._add_model(db.Vacancy, v)
        return "vacancy was added"

    @classmethod
    def add_comp(cls, c: Company) -> str:
        cls._add_model(db.Company, c)
        return "company was added"

    @classmethod
    def add_cat(cls, c: Category) -> str:
        cls._add_model(db.Category, c)
        return "category was added"



@app.post("/vacancy")
def add_vacs(v_di: Annotated[str, Depends(AddDependency.add_vac)]) -> str:
    return v_di

@app.post("/company")
def add_comps(c_di: Annotated[str, Depends(AddDependency.add_comp)]) -> str:
    return c_di

@app.post("/category")
def add_cats(c_di: Annotated[str, Depends(AddDependency.add_cat)]) -> str:
    return c_di





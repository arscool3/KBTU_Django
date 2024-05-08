from contextlib import contextmanager
from typing import Optional, Annotated

from sqlalchemy import select
from fastapi import FastAPI, HTTPException, Depends

from entity import Box, Chocolate #ChocolateWithBoxId
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


@app.get("/box")
def box(id: int) -> Box:
    with get_db() as session:
        box = session.get(db.Box, id)
        if box is None:
            raise HTTPException(status_code=404)
        return Box.model_validate(box)


@app.get("/boxes")
def boxes() -> list[Box]:
    with get_db() as session:
        db_boxes = session.execute(select(db.Box)).scalars().all()
        boxes = []
        for db_box in db_boxes:
            boxes.append(box.model_validate(db_box))
        return boxes


class AddDependency:

    @staticmethod
    def _add_model(db_model: type[db.Box] | type[db.Chocolate], pydantic_model: Box | Chocolate) -> None:
        with get_db() as session:
            session.add(db_model(**pydantic_model.model_dump()))

    @classmethod
    def add_box(cls, box: Box) -> str:
        cls._add_model(db.Box, box)
        return "box was added"

    @classmethod
    def add_chocolate(cls, chocolate: Chocolate) -> str:
        cls._add_model(db.Chocolate, chocolate)
        return "chocolate was added"


@app.post("/box")
def add_box(box_di: Annotated[str, Depends(AddDependency.add_box)]) -> str:
    return box_di


@app.post("/chocolate")
def add_chocolate(chocolate_di: Annotated[str, Depends(AddDependency.add_chocolate)]) -> str:
    return chocolate_di


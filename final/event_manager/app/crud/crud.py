from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import DeclarativeMeta
from typing import Type, TypeVar, List, Union

ModelType = TypeVar("ModelType", bound=DeclarativeMeta)

def get_by_id(db: Session, model: Type[ModelType], item_id: int) -> Union[ModelType, None]:
    return db.query(model).filter(model.id == item_id).first()

def get_all(db: Session, model: Type[ModelType]) -> List[ModelType]:
    return db.query(model).all()

def create(db: Session, model: Type[ModelType], obj_in) -> ModelType:
    db_obj = model(**obj_in.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update(db: Session, model: Type[ModelType], item_id: int, obj_in) -> Union[ModelType, None]:
    db_obj = get_by_id(db, model, item_id)
    if db_obj:
        for attr, value in obj_in.dict(exclude_unset=True).items():
            setattr(db_obj, attr, value)
        db.commit()
        db.refresh(db_obj)
    return db_obj

def delete(db: Session, model: Type[ModelType], item_id: int) -> Union[ModelType, None]:
    db_obj = get_by_id(db, model, item_id)
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj

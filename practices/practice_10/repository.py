from abc import abstractmethod
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.orm import Session

import models as db
from schemas import Star, Satellite, Planet, ReturnType


class AbcRepository:

    @abstractmethod
    def __init__(self, session: Session):
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> ReturnType:
        raise NotImplementedError()


class StarRepository(AbcRepository):
    def __init__(self, session: Session):
        self._session = session

    def get_by_id(self, id: int) -> Star:
        print(2)
        db_star = self._session.get(db.Star, id)
        print(db_star)
        return Star.model_validate(db_star)


class PlanetRepository(AbcRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, id: int) -> Planet:
        print(2)
        db_planet = self._session.get(db.Planet, id)
        print(db_planet)
        return Planet.model_validate(db_planet)


class SatelliteRepository(AbcRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, id: int) -> Satellite:
        print(2)
        db_satellite = self._session.get(db.Satellite, id)
        print(db_satellite)
        return Satellite.model_validate(db_satellite)
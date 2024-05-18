import punq
from fastapi.params import Depends
from pydantic import BaseModel
from sqlalchemy import select, insert
from fastapi import FastAPI

import models as db
from database import session
from schemas import Star, Satellite, Planet, StarCreate, SatelliteCreate, PlanetCreate, ReturnType
from repository import StarRepository, AbcRepository, PlanetRepository, SatelliteRepository

app = FastAPI()


class Dependency:
    def __init__(self, repo: AbcRepository):
        self.repo = repo

    def __call__(self, id: int) -> ReturnType:
        return self.repo.get_by_id(id)


def get_container(repository: type[AbcRepository]) -> punq.Container:
    container = punq.Container()
    container.register(AbcRepository, repository, instance=repository(session=session))
    container.register(Dependency)
    return container


app.add_api_route("/stars", get_container(StarRepository).resolve(Dependency), methods=["GET"])
app.add_api_route("/planets", get_container(PlanetRepository).resolve(Dependency), methods=["GET"])
app.add_api_route("/satellites", get_container(SatelliteRepository).resolve(Dependency), methods=["GET"])



@app.post("/stars")
def add_citizens(star: StarCreate) -> str:
    session.add(db.Star(**star.model_dump()))
    session.commit()
    session.close()
    return "Star was added"


@app.post("/planet")
def add_country(planet: PlanetCreate) -> str:
    session.add(db.Planet(**planet.model_dump()))
    session.commit()
    session.close()
    return "Planet was added"


@app.post("/satellite")
def add_president(satellite: SatelliteCreate) -> str:
    session.add(db.Satellite(**satellite.model_dump()))
    session.commit()
    session.close()
    return "Satellite was added"
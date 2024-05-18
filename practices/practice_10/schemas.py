from pydantic import BaseModel
from typing import List


class SpaceObjectBase(BaseModel):
    name: str
    weight: int
    radius: int

    class Config:
        from_attributes = True


class StarCreate(SpaceObjectBase):
    temperature: int


class Star(StarCreate):
    id: int


class PlanetBase(SpaceObjectBase):
    habitable: bool

    class Config:
        from_attributes = True


class PlanetCreate(PlanetBase):
    star_id: int


class Planet(PlanetBase):
    id: int
    star: Star


class SatelliteBase(SpaceObjectBase):
    habitable: bool
    planet_id: int

    class Config:
        from_attributes = True


class SatelliteCreate(SatelliteBase):
    pass


class Satellite(SatelliteBase):
    id: int
    planet: Planet


class ResidentBase(BaseModel):
    name: str

    class Config:
        from_attributes = True


class ResidentCreate(ResidentBase):
    planet_ids: List[int]


class Resident(ResidentBase):
    id: int
    planets: List[Planet]


ReturnType = Satellite | Star | Planet
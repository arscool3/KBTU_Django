# pip install fastapi uvicorn pydantic
from datetime import datetime
from fastapi import FastAPI
from enum import Enum
import pydantic

app = FastAPI()

class AnimalType(Enum):
    tiger = "tiger"
    alligator = "alligator"
    monkey = "monkey"

class Animal(pydantic.BaseModel):
    type: AnimalType
    amount: int = pydantic.Field(gt=1)

class Zoo(pydantic.BaseModel):
    animals: str 
    size: int 

animals = []
zoos = []

@app.get("/zoo")
def getZoos():
    return {"zoos": zoos}

@app.post("/zoo")
def postZoo(zoo: Zoo):
    zoos.append(zoo)
    return zoos

# @app.delete("/zoo/:id")
# def deleteZoo(zooId: int):
    

@app.get('/')
def getAnimals():
    return {"animals": animals}

@app.post('/')
def postAnimals(animal: Animal) -> list[Animal]:
    animals.append(animal)
    return animals
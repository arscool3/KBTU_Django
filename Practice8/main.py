from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Person(BaseModel):
    name: str
    surname: str
    age: int


people = []


@app.get("/people/")
async def get_people():
    return people


@app.get("/people/{index}")
async def get_person(index: int):
    if index < 0 or index >= len(people):
        raise HTTPException(status_code=404, detail="Person not found")
    return people[index]


@app.post("/people/")
async def create_person(person: Person):
    people.append(person)
    return person


@app.put("/people/{index}")
async def update_person(index: int, updated_person: Person):
    if index < 0 or index >= len(people):
        raise HTTPException(status_code=404, detail="Person not found")
    people[index] = updated_person
    return updated_person


@app.delete("/people/{index}")
async def delete_person(index: int):
    if index < 0 or index >= len(people):
        raise HTTPException(status_code=404, detail="Person not found")
    deleted_person = people.pop(index)
    return {"message": "Person deleted successfully", "deleted_person": deleted_person}
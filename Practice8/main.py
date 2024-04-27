from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Aircraft(BaseModel):
    id: int
    aircraft_code: str
    full_name: Optional[str]
    short_name: Optional[str]
    built_date: Optional[str]
    full_capacity: Optional[int]
    economy_capacity: Optional[int]
    business_capacity: Optional[int]
    owner_airline: Optional[int]


aircrafts = []

@app.get("/aircrafts", response_model=List[Aircraft])
def get_aircrafts():
    return aircrafts

@app.get("/aircrafts/{aircraft_id}", response_model=Aircraft)
def get_aircraft(aircraft_id: int):
    for aircraft in aircrafts:
        if aircraft["id"] == aircraft_id:
            return aircraft
    raise HTTPException(status_code=404, detail="Aircraft not found")

@app.post("/aircrafts", response_model=Aircraft)
def create_aircraft(aircraft: Aircraft):
    aircraft_data = aircraft.model_dump()
    aircrafts.append(aircraft_data)
    return aircraft_data

@app.put("/aircrafts/{aircraft_id}", response_model=Aircraft)
def update_aircraft(aircraft_id: int, aircraft: Aircraft):
    for i, aircraft_data in enumerate(aircrafts):
        if aircraft_data["id"] == aircraft_id:
            aircrafts[i] = aircraft.model_dump()
            aircrafts[i]["id"] = aircraft_id
            return aircrafts[i]
    raise HTTPException(status_code=404, detail="Aircraft not found")

@app.delete("/aircrafts/{aircraft_id}")
def delete_aircraft(aircraft_id: int):
    for i, aircraft_data in enumerate(aircrafts):
        if aircraft_data["id"] == aircraft_id:
            del aircrafts[i]
            return {"message": "Aircraft deleted successfully"}
    raise HTTPException(status_code=404, detail="Aircraft not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
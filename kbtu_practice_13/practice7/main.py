from fastapi import FastAPI, HTTPException
from dramatiq.results.errors import ResultMissing
import random

from tasks import get_weather_task, result_backend

app = FastAPI()

CITIES = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia"]


@app.post("/weather")
async def get_weather(city: str) -> dict:
    if city not in CITIES:
        raise HTTPException(status_code=404, detail="City not found")

    task = get_weather_task.send(city)

    return {"task_id": task.message_id}


@app.get("/weather_status")
async def get_weather_status(task_id: str) -> dict:
    try:
        weather_data = result_backend.get_result(get_weather_task.message().copy(message_id=task_id))
    except ResultMissing:
        raise HTTPException(status_code=404, detail="Weather data not found")

    return weather_data

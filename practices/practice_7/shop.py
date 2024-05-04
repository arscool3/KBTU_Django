from fastapi import FastAPI
from dramatiq.results.errors import ResultMissing

from tasks import get_timezone

app = FastAPI()

@app.get("/get_city/{city}")
def get_city_timezone(city: str):
    result = get_timezone.send(city)
    try:
        timezone_result = result.get_result()
        return {"timezone": timezone_result}
    except ResultMissing:
        return {"error": "Task result not found"}

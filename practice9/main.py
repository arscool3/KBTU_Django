from fastapi import FastAPI, Depends
from datetime import datetime

app = FastAPI()


# Dependency function to get the current time
async def get_current_time() -> datetime:
    return datetime.now()


def generate_greeting(current_time: datetime = Depends(get_current_time)):
    if current_time.hour < 12:
        greeting = "Good morning!"
    elif current_time.hour < 18:
        greeting = "Good afternoon!"
    else:
        greeting = "Good evening!"
    return greeting


@app.get("/greeting")
async def get_greeting(greeting: str = Depends(generate_greeting)):
    return {"greeting": greeting}

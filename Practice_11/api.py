import asyncio
import random

from fastapi import FastAPI, WebSocket

app = FastAPI()


cities = ["Almaty", "Shymkent", "Astana", "Karagandy", "Atyrau", "Taldykorgan"]

# Weather conditions
weather_conditions = ["Sunny", "Rainy", "Cloudy", "Snowy", "Windy"]


@app.websocket("/weather")
async def weather_updates(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            city = random.choice(cities)
            condition = random.choice(weather_conditions)
            temperature = random.randint(-10, 35)
            await websocket.send_json({city: {"condition": condition, "temperature": temperature}})
            await asyncio.sleep(2)
    except Exception as e:
        print(f'Error: {e}')
    finally:
        await websocket.close()
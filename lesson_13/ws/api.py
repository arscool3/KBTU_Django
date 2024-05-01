import asyncio
import random

from fastapi import FastAPI, WebSocket

app = FastAPI()


@app.get('/test')
def test() -> str:
    return 'OK'


cities = [
    "Almaty", "Astana", "Wuhan", "Hong Kong", "Tokyo"
]


@app.websocket("/earthquake")
async def earthquake(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            await websocket.send_json({random.choice(cities): random.randint(1, 9)})
            await asyncio.sleep(1)
    except Exception as e:
        print(f'Error {e}')
    finally:
        await websocket.close()

# pip install websockets

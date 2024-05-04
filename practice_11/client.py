import asyncio
import json

import websockets


async def client():
    url = "ws://127.0.0.1:8000/course_news"
    async with websockets.connect(url) as websocket:
        while True:
            data = await websocket.recv()
            print(f"News received: {json.loads(data)}")



asyncio.run(client())
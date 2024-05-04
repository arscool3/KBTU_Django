import asyncio
import json

import websockets


async def client():
    url = "ws://127.0.0.1:8000/earthquake"
    async with websockets.connect(url) as websocket:
        while True:
            data = await websocket.recv()
            print(f"Received data: {json.loads(data)}")



asyncio.run(client())
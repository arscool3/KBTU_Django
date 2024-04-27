import asyncio
import websockets
import json

async def data_client():
    uri = "ws://127.0.0.1:8000/data"
    async with websockets.connect(uri) as websocket:
        while True:
            data = await websocket.recv()
            print(f"Received data: {json.loads(data)}")

asyncio.run(data_client())
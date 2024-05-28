import asyncio
import json
import websockets


async def client():
    url = "ws://127.0.0.1:8000/weather"
    async with websockets.connect(url) as websocket:
        while True:
            data = await websocket.recv()
            print(f"Received data: {json.loads(data)}")

if __name__ == "__main__":
    asyncio.run(client())
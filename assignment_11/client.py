import asyncio
import websockets

async def client():
    url = "ws://127.0.0.1:8000/time"
    async with websockets.connect(url) as websocket:
        print("Connected to server")
        while True:
            server_time = await websocket.recv()
            print(f"Received from server: {server_time}")

asyncio.run(client())

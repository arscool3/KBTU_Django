import asyncio
import websockets

async def chat_client():
    async with websockets.connect("ws://127.0.0.1:8000/chat") as websocket:
        while True:
            response = await websocket.recv()
            print("Received from Client 1:", response)
            message = input("Client 2: Enter message: ")
            await websocket.send(f"{message}")

asyncio.run(chat_client())

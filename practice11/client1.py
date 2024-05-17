import asyncio
import websockets

async def chat_client():
    async with websockets.connect("ws://127.0.0.1:8000/chat") as websocket:
        while True:
            message = input("Client 1: Enter message: ")
            await websocket.send(f"{message}")
            response = await websocket.recv()
            print("Received from Client 2:", response)

asyncio.run(chat_client())
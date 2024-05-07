import asyncio
import websockets


async def chat_user():
    async with websockets.connect("ws://127.0.0.1:8000/chat") as websocket:
        while True:
            response = await websocket.recv()
            print("Received from User 1:", response)
            message = input("User 2: Enter message: ")
            await websocket.send(f"{message}")

asyncio.run(chat_user())
import asyncio
import websockets

async def send_message():
    async with websockets.connect("ws://localhost:8000/ws") as websocket:
        message = input("Enter a message to send: ")
        await websocket.send(message)
        response = await websocket.recv()
        print(f"Received response: {response}")

asyncio.run(send_message())

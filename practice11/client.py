import asyncio
import websockets

async def chat_client(room_id):
    url = f"ws://localhost:8000/ws/{room_id}"
    async with websockets.connect(url) as websocket:
        while True:
            message = await websocket.recv()
            print(message)

async def send_messages(room_id):
    url = f"ws://localhost:8000/ws/{room_id}"
    async with websockets.connect(url) as websocket:
        while True:
            message = input("Enter message to send: ")
            await websocket.send(message)

async def main():
    room_id = input("Enter room ID to join: ")
    await asyncio.gather(chat_client(room_id), send_messages(room_id))

asyncio.run(main())

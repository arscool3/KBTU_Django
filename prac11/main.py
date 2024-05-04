import asyncio
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import websockets


app = FastAPI()

async def hello():
    name = input("Enter your name: ")
    print(f"message: Hello, {name}")

async def send_messages():
    try:
        async with websockets.connect("ws://127.0.0.1:8000/ws") as websocket:
            for i in range(5):
                message = f"Test message {i+1}"
                await websocket.send(message)
                print(f"Sent: {message}")
                response = await websocket.recv()
                print(f"Received: {response}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(send_messages())
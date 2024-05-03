import asyncio
import websockets


async def connect_to_websocket():
    uri = "ws://127.0.0.1:8000/orders/ws"
    async with websockets.connect(uri) as websocket:
        print("WebSocket connection established.")
        try:
            while True:
                message = await websocket.recv()
                print("Received message:", message)
        except websockets.ConnectionClosed:
            print("WebSocket connection closed.")


asyncio.run(connect_to_websocket())

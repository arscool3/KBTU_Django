import asyncio
from fastapi import WebSocket
from fastapi.routing import WebSocketRoute
from main import app

# Define WebSocket route
@app.websocket_route("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        try:
            data = await websocket.receive_text()
            await websocket.send_text(f"Message received: {data}")
        except Exception as e:
            print(f"WebSocket error: {e}")
            break

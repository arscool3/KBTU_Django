import asyncio
from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await asyncio.sleep(1)  # sleep for 1 second
        await websocket.send_text(f"Message text was: {data}")

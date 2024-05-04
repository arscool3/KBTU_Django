from fastapi import FastAPI, WebSocket
from datetime import datetime
import asyncio

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            current_time = datetime.now()
            await websocket.send_text(f"Received message: {data}, Current time: {current_time}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        await websocket.close()
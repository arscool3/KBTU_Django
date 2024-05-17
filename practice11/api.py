import asyncio
from typing import List
from fastapi import FastAPI, WebSocket

app = FastAPI()
connected_clients: List[WebSocket] = []


@app.websocket("/chat")
async def websocket_chat(websocket: WebSocket):
    # Принимаем нового клиента
    await websocket.accept()
    connected_clients.append(websocket)
    try:
        while True:
            message = await websocket.receive_text()
            for client in connected_clients:
                if client != websocket:
                    await client.send_text(message)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        connected_clients.remove(websocket)
        await websocket.close()

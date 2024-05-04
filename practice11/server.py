import asyncio
from fastapi import FastAPI, WebSocket
from typing import Dict

app = FastAPI()

room_connections: Dict[str, list] = {}

@app.websocket("/ws/{room_id}")
async def websocket_endpoint(websocket: WebSocket, room_id: str):
    await websocket.accept()
    if room_id not in room_connections:
        room_connections[room_id] = []
    room_connections[room_id].append(websocket) 
    try:
        while True:
            message = await websocket.receive_text()  
            for conn in room_connections[room_id]:
                await conn.send_text(message)
    except Exception as e:
        print(f"WebSocket connection closed with error: {e}")
    finally:
        room_connections[room_id].remove(websocket)  

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

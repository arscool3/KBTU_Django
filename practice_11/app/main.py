from fastapi import FastAPI, WebSocket
from typing import List

app = FastAPI()

# Store connected websocket clients
websocket_clients: List[WebSocket] = []

# WebSocket endpoint to connect clients
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    websocket_clients.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            # Broadcast received data to all connected clients
            for client in websocket_clients:
                await client.send_text(data)
    except Exception:
        websocket_clients.remove(websocket)

# Start the application using uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

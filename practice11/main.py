from fastapi import FastAPI, WebSocket

app = FastAPI()

# Create a dictionary to store active websocket connections
active_connections = {}

# WebSocket endpoint
@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await websocket.accept()
    active_connections[client_id] = websocket
    try:
        while True:
            # Receive data from client
            data = await websocket.receive_text()
            # Broadcast data to all connected clients
            for connection_id, connection in active_connections.items():
                if connection_id != client_id:
                    await connection.send_text(f"Client {client_id}: {data}")
    except Exception as e:
        print(f"Client {client_id} disconnected")
        del active_connections[client_id]

from fastapi import FastAPI, WebSocket

app = FastAPI()

connected_clients = []

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    connected_clients.append(websocket)

    try:
    
        await websocket.send_text("Welcome to the WebSocket connection!")

        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"You sent: {data}")
    except Exception as e:
        print(f"WebSocket connection closed with error: {e}")
    finally:
        connected_clients.remove(websocket)


from typing import List
from fastapi import FastAPI, WebSocket

app = FastAPI()
connected_users: List[WebSocket] = []


@app.websocket("/chat")
async def websocket_chat(websocket: WebSocket):
    await websocket.accept()
    connected_users.append(websocket)
    try:
        while True:
            message = await websocket.receive_text()
            for user in connected_users:
                if user != websocket:
                    await user.send_text(message)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        connected_users.remove(websocket)
        await websocket.close()

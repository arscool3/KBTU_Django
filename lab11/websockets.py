from fastapi import WebSocket, APIRouter

websocket_router = APIRouter()

async def echo_message(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Echoed message: {data}")

@websocket_router.websocket("/echo")
async def websocket_echo_endpoint(websocket: WebSocket):
    await echo_message(websocket)
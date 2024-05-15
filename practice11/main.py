from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()

connections = {}

@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    try:
        await ws.send_text("Welcome to chat! Enter your name:")
        name = await ws.receive_text()

        await broadcast(f"{name} joined the chat.", sender=name)

        while True:
            message = await ws.receive_text()
            await handle_message(name, message)
    except WebSocketDisconnect:
        del connections[name]
        await broadcast(f"{name} left the chat.")
    except Exception as e:
        print('Error:', e)

async def broadcast(message: str, sender: str = None):
    for name, connection in connections.items():
        if sender != name:
            await connection.send_text(message)

async def handle_message(sender: str, message: str):
    if message.startswith("@"):
        recipient, msg = message[1:].split(":", 1)
        recipient = recipient.strip()
        if recipient in connections:
            await connections[recipient].send_text(f"(Private) {sender}: {msg}")
        else:
            await connections[sender].send_text(f"User '{recipient}' is not online.")
    else:
        await broadcast(f"{sender}: {message}", sender)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

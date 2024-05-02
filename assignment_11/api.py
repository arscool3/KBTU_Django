from fastapi import FastAPI, WebSocket
import datetime
import asyncio

app = FastAPI()

@app.websocket("/time")
async def time_websocket(websocket: WebSocket):
    print("Client connected")
    await websocket.accept()
    try:
        while True:
            now = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sending time: {now}")
            await websocket.send_text(f"Server time: {now}")
            await asyncio.sleep(1)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Client disconnected")
        await websocket.close()

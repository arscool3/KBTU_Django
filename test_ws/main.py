from fastapi import FastAPI, WebSocket
import asyncio
import random

app = FastAPI()
cnt = 0

@app.websocket("/data")
async def data_stream(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            global cnt
            # Simulating real-time data update, e.g., stock prices
            price = random.randint(100, 200)
            cnt += 1
            if cnt == 10:
                raise Exception('123')
            await websocket.send_json({"stock": "XYZ", "price": price})
            await asyncio.sleep(1)  # send updates every second

    except Exception as e:
        print(f"Error: {e}")
    finally:
        await websocket.close()
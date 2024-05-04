import asyncio
import json
import websockets
from fastapi import FastAPI

app = FastAPI()
async def stock_client(user_id):
    url = "ws://127.0.0.1:8000/stocks"
    async with websockets.connect(url) as websocket:
        try:
            while True:
                data = await websocket.recv()
                stock_data = json.loads(data)
                symbol = stock_data["symbol"]
                company = stock_data["company"]
                price = stock_data["price"]
                print(f"User {user_id}: Received stock update for {company} ({symbol}): ${price}")
        except websockets.exceptions.ConnectionClosed:
            print(f"User {user_id}: Connection closed. Reconnecting...")
            await asyncio.sleep(1)
            await stock_client(user_id)

async def main():
    num_users = 3  # Number of WebSocket clients (simulated users)
    tasks = [stock_client(user_id) for user_id in range(1, num_users + 1)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())

import asyncio
import json
import websockets

async def stock_client():
    url = "ws://127.0.0.1:8000/stocks"
    async with websockets.connect(url) as websocket:
        while True:
            data = await websocket.recv()
            stock_data = json.loads(data)
            symbol = stock_data["symbol"]
            company = stock_data["company"]
            price = stock_data["price"]
            print(f"Received stock update for {company} ({symbol}): ${price}")

asyncio.run(stock_client())

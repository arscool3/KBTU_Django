import asyncio
import random

from fastapi import FastAPI, WebSocket

app = FastAPI()

# Sample stock symbols and their respective companies
stocks = {
    "AAPL": "Apple Inc.",
    "GOOGL": "Alphabet Inc.",
    "MSFT": "Microsoft Corporation"
}

@app.websocket("/stocks")
async def stock_updates(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            symbol = random.choice(list(stocks.keys()))
            price = round(random.uniform(100, 500), 2)  # Generate a random stock price
            message = {
                "symbol": symbol,
                "company": stocks[symbol],
                "price": price
            }
            await websocket.send_json(message)
            await asyncio.sleep(1)  # Send updates every second
    except Exception as e:
        print(f'Error in stock_updates: {e}')
    finally:
        await websocket.close()

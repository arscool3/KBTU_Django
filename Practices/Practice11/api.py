import asyncio
import random

from fastapi import FastAPI, WebSocket

app = FastAPI()

Companies = [
    {"company": "Apple", "capitalization": 900},
    {"company": "Ford", "capitalization": 100},
    {"company": "Google", "capitalization": 1000},
    {"company": "Samsung", "capitalization": 200},
]


def ShowChange():
    change = (random.randint(1, 100) / 100) * random.choice([1, -1])
    comp = random.choice(Companies)
    return (comp.get("company"),
            comp.get("capitalization") + comp.get("capitalization") * change, change)


@app.websocket("/market_change")
async def marketChange(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = ShowChange()
            await websocket.send_json({'company' : data[0], 'current_capitalization': data[1], "change": data[2]})
            await asyncio.sleep(1)
    except Exception as e:
        print(f'Error {e}')
    finally:
        await websocket.close()
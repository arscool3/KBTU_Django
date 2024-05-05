import asyncio
import random
from fastapi import APIRouter, WebSocket, WebSocketDisconnect

router = APIRouter()

@router.get('/test')
def test() -> str:
    return 'OK'

products = [
    {"name": "Foundation", "brand": "Maybelline", "price": 10.99},
    {"name": "Mascara", "brand": "L'Oréal", "price": 8.99},
    {"name": "Lipstick", "brand": "MAC", "price": 14.99},
    {"name": "Eyeshadow Palette", "brand": "Urban Decay", "price": 39.99},
    {"name": "Blush", "brand": "NARS", "price": 24.99}
]

@router.websocket("/sales")
async def sales(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            product = random.choice(products)
            await websocket.send_json(product)
            await asyncio.sleep(1)
    except WebSocketDisconnect:
        print("Client disconnected")
    except Exception as e:
        print(f'Error {e}')
    finally:
        await websocket.close()

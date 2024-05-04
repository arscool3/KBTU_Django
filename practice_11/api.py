import asyncio
import random

from fastapi import FastAPI, WebSocket

app = FastAPI()


instructors = ['Main', 'New', 'Practice Teacher']
news = ['New Assignment', 'Course Update', 'New Course', 'Assignment returned']


@app.websocket("/course_news")
async def earthquake(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            await websocket.send_json({random.choice(instructors): random.choice(news)})
            await asyncio.sleep(3)
    except Exception as e:
        print(f'Error {e}')
    finally:
        await websocket.close()

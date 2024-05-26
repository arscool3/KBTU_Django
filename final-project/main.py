from fastapi import FastAPI
from dramatiq import set_broker
from dramatiq.brokers.redis import RedisBroker
from app.api import book, user, author, auth, review
from app.tasks.background_tasks import BackgroundTasks

app = FastAPI()

broker = RedisBroker(host="localhost", port=6379)
set_broker(broker)

app.include_router(book.router)
app.include_router(user.router)
app.include_router(author.router)
app.include_router(auth.router)
app.include_router(review.router)


background_tasks = BackgroundTasks()


@app.on_event("startup")
async def startup_event():
    background_tasks.start()


@app.on_event("shutdown")
async def shutdown_event():
    background_tasks.stop()

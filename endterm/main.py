import asyncio

from fastapi import FastAPI
from routes.user import router as UserRouter
from routes.payment import router as PaymentRouter

from database import init_db

app = FastAPI(debug=True)

app.include_router(UserRouter, tags=["User"], prefix="/api/v1/users")
app.include_router(PaymentRouter, tags=["Payment"], prefix="/api/v1/users")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to gbdqPay. Check /docs for more info"}


@app.get("/health", tags=["Root"])
async def health_check():
    return {"detail": "OK"}

@app.on_event("startup")
async def start_db():
    await init_db()

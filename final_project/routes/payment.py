from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from services import payment

router = APIRouter()


@router.get("/")
async def hello_payment():
    return "hello payment"


@router.post("/create")
async def create_payment():
    return await payment.create_payment()

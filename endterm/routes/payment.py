from fastapi import APIRouter, Depends

router = APIRouter()



@router.get("/")
async def hello_payment():
    return "hello payment"
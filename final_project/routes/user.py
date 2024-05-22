from fastapi import APIRouter, Depends

router = APIRouter()



@router.get("/me")
async def get_current_user():
    return "user"
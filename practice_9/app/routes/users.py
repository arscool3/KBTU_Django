from fastapi import APIRouter, Depends
from ..dependencies.users import get_current_user

router = APIRouter()

@router.get("/users/me")
async def read_users_me(current_user: str = Depends(get_current_user)):
    return {"current_user": current_user}

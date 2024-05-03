from fastapi import APIRouter, Depends
from ..dependencies.database import get_db

router = APIRouter()

@router.get("/items/")
async def read_items(db=Depends(get_db)):
    return {"db_status": db}

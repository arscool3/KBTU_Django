from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from ..database import get_db
from .service import get_activities_by_username

router = APIRouter(prefix="/activity", tags=["activity"])


@router.get("/user/{username}")
async def activity(
    username: str, page: int = 1, limit: int = 10, db: Session = Depends(get_db)
):
    return await get_activities_by_username(db, username, page, limit)

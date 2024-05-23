from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel
from app.auth.user import get_current_user
from app.db.database import get_db
from app.models.stream import Stream
from app.models.user import User

router = APIRouter()

class StreamCreate(BaseModel):
    title: str
    description: str
    user_id: int

@router.post("/")
async def create_stream(stream: StreamCreate, db: AsyncSession = Depends(get_db), user: User = Depends(get_current_user)):
    db_stream = Stream(title=stream.title, description=stream.description, user_id=user.id)
    db.add(db_stream)
    await db.commit()
    await db.refresh(db_stream)
    return db_stream

@router.get("/{stream_id}")
async def get_stream(stream_id: int, db: AsyncSession = Depends(get_db)):
    stream = await db.get(Stream, stream_id)
    if not stream:
        raise HTTPException(status_code=404, detail="Stream not found")
    return stream

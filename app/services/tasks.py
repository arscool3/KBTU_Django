import logging
import dramatiq

from dramatiq.brokers.redis import RedisBroker
from dramatiq.results import Results
from dramatiq.results.backends.redis import RedisBackend

from fastapi import Depends, HTTPException
from app.db.database import SessionLocal, get_db
from app.models.video import Video
from app.models.user import User
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

result_backend = RedisBackend()
redis_broker = RedisBroker()
redis_broker.add_middleware(Results(backend=result_backend))
dramatiq.set_broker(redis_broker)

@dramatiq.actor
async def process_video(video_data: dict, user_id: int,  db: AsyncSession = Depends(get_db)):
    user = await db.get(User, user_id)
    
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    video_db = Video(title=video_data.title, description=video_data.description, url=video_data.url, user_id=user_id)
    db.add(video_db)

    await db.commit()
    await db.refresh(video_db)

    return video_db
    

    
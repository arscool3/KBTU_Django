from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel
from app.db.database import get_db
from app.models.video import Video
from app.schemas.video import VideoBase
from app.models.comment import Comment  # Import the Comment model
from app.models.user import User
from app.services.tasks import process_video
from app.auth.user import get_current_user
from typing import List 
from sqlalchemy.future import select

router = APIRouter()

class VideoCreate(BaseModel):
    title: str
    description: str
    url: str

@router.post("/")
async def create_video(video: VideoCreate, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    process_video.send(video.model_dump(), int(current_user.id))
    return {"message": "Video processing started successfully"}

@router.get("/", response_model=List[VideoBase])
async def get_all_videos(db: AsyncSession = Depends(get_db)):
    # Retrieve all users from the database
    videos = await db.execute(select(Video))
    return videos.scalars().all()

@router.get("/{video_id}")
async def get_video(video_id: int, db: AsyncSession = Depends(get_db)):
    # Retrieve the video from the database
    video = await db.get(Video, video_id)
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")
    
    # Retrieve comments associated with the video
    comments = await db.execute(select(Comment).filter(Comment.video_id == video_id))
    video_data = video.__dict__
    
    # Convert comments to a list of dictionaries
    comments_data = [comment.__dict__ for comment in comments.scalars()]
    
    # Include comments in the response
    video_data["comments"] = comments_data
    
    return video_data

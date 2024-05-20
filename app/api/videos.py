from fastapi import APIRouter, UploadFile, Depends, File
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.video import Video
from app.db.session import get_session
from app.services.tasks import trigger_video_processing

router = APIRouter()

@router.post("/upload")
async def upload_video(file: UploadFile = File(...), session: AsyncSession = Depends(get_session)):
    # Save the file locally or to a cloud storage
    video = Video(title=file.filename, description="Video description", user_id=current_user.id)
    session.add(video)
    await session.commit()
    await session.refresh(video)

    # Trigger background task for video processing
    trigger_video_processing(video.id)
    return {"filename": file.filename}

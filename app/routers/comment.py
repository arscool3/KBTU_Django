from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel
from app.auth.user import get_current_user
from app.db.database import get_db
from app.models.comment import Comment
from app.models.user import User
from app.models.video import Video

router = APIRouter()

class CommentCreate(BaseModel):
    content: str

@router.post("/{video_id}/comments")
async def create_comment(comment: CommentCreate, video_id: int, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_comment = Comment(content=comment.content, user_id=current_user.id, video_id=video_id)
    db.add(db_comment)
    await db.commit()
    await db.refresh(db_comment)
    return db_comment

@router.get("/{video_id}/comments/{comment_id}")
async def get_comment(comment_id: int, db: AsyncSession = Depends(get_db) ):
    
    #can do something using video_id, but right now nothing comes to mind
    comment = await db.get(Comment, comment_id)
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    return comment

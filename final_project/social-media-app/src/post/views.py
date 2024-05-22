from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from .schemas import PostCreate, Post
from .service import (
    create_post_svc,
    delete_post_svc,
    create_hashtags_svc,
    get_post_from_post_id_svc,
    get_posts_from_hashtag_svc,
    get_random_posts_svc,
    get_user_posts_svc,
    like_post_svc,
    unlike_post_svc,
    liked_users_post_svc,
)
from ..auth.service import get_current_user, existing_user
from ..auth.schemas import User

router = APIRouter(prefix="/posts", tags=["posts"])


@router.post("/", response_model=Post, status_code=status.HTTP_201_CREATED)
async def create_post(post: PostCreate, token: str, db: Session = Depends(get_db)):
    # verify the token
    user = await get_current_user(db, token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="you are not authorized."
        )

    # create post
    db_post = await create_post_svc(db, post, user.id)

    return db_post


@router.get("/user", response_model=list[Post])
async def get_current_user_posts(token: str, db: Session = Depends(get_db)):
    # verify the token
    user = await get_current_user(db, token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="you are not authorized."
        )

    return await get_user_posts_svc(db, user.id)


@router.get("/user/{username}", response_model=list[Post])
async def get_user_posts(username: str, db: Session = Depends(get_db)):
    # verify token
    user = await existing_user(db, username, "")

    return await get_user_posts_svc(db, user.id)


@router.get("/hashtag/{hashtag}")
async def get_posts_from_hashtag(hashtag: str, db: Session = Depends(get_db)):
    return await get_posts_from_hashtag_svc(db, hashtag)


@router.get("/feed")
async def get_random_posts(
    page: int = 1, limit: int = 5, hashtag: str = None, db: Session = Depends(get_db)
):
    return await get_random_posts_svc(db, page, limit, hashtag)


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(token: str, post_id: int, db: Session = Depends(get_db)):
    # verify the token
    user = await get_current_user(db, token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="you are not authorized to delete this post.",
        )

    post = await get_post_from_post_id_svc(db, post_id)
    if post.author_id != user.id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="you are not authorized to delete this post.",
        )

    await delete_post_svc(db, post_id)


@router.post("/like", status_code=status.HTTP_204_NO_CONTENT)
async def like_post(post_id: int, username: str, db: Session = Depends(get_db)):
    res, detail = await like_post_svc(db, post_id, username)
    if res == False:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=detail)


@router.post("/unlike", status_code=status.HTTP_204_NO_CONTENT)
async def like_post(post_id: int, username: str, db: Session = Depends(get_db)):
    res, detail = await unlike_post_svc(db, post_id, username)
    if res == False:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=detail)


@router.get("/likes/{post_id}", response_model=list[User])
async def users_like_post(post_id: int, db: Session = Depends(get_db)):
    return await liked_users_post_svc(db, post_id)


@router.get("/{post_id}", response_model=Post)
async def get_post(post_id: int, db: Session = Depends(get_db)):
    db_post = await get_post_from_post_id_svc(db, post_id)
    if not db_post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="invalid post id"
        )

    return db_post

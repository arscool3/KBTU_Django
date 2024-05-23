from fastapi import APIRouter
from typing import Annotated, Any
from fastapi import Depends
from database import get_db
from utils.auth_utils import require_scope
from crud.news_crud import *
from schemas import news_schemas as schemas

router = APIRouter(
    prefix='/news',
    tags=['news']
)


@router.post("/")
def create_news(news: schemas.NewsCreate, session: Annotated[str, Depends(get_db)], scope: Annotated[Any, Depends(require_scope("instructor"))]):
    create_news(news, session)

    return {"message": "news successfully created"}


@router.get("/")
def get_news_lists(session: Annotated[str, Depends(get_db)]):
    news = get_all_news(session)

    return {"news": news}


@router.get("/{news_id}")
def get_news_by_id(news_id: int, session: Annotated[str, Depends(get_db)]):
    news = get_news_by_id(news_id, session)

    return {"news": news}






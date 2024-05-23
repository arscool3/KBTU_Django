from typing import Annotated
from fastapi import Depends
from database import get_db
from models import news_models as models
from schemas import news_schemas as schemas

def create_news(news: schemas.NewsCreate, session: Annotated[str, Depends(get_db)]):
    new_news = models.News(author_id=news.author_id, title=news.title, text=news.text, date=news.date)

    session.add(new_news)
    session.commit()
    session.refresh(new_news)

    return new_news


def get_news_by_id(news_id: int, session: Annotated[str, Depends(get_db)]):
    return session.query(models.News).filter(models.News.id==news_id).first()


def get_all_news(session: Annotated[str, Depends(get_db)]):
    return session.query(models.News)



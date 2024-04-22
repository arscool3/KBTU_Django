from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Article(BaseModel):
    id: int
    title: str
    author: str

articles: List[Article] = []

@app.get("/articles", response_model=List[Article])
def get_articles():
    return articles

@app.post("/articles", response_model=Article)
def create_article(article: Article):
    if any(a.id == article.id for a in articles):
        raise HTTPException(status_code=400, detail="Article with this id already exists")
    articles.append(article)
    return article

@app.put("/articles/{id}", response_model=Article)
def update_article(article_id: int, updated_article: Article):
    for i, article in enumerate(articles):
        if article.id == article_id:
            articles[i] = updated_article
            return updated_article
    raise HTTPException(status_code=404, detail="Article not found")

@app.delete("/articles/{id}", response_model=Article)
def delete_article(article_id: int):
    for i, article in enumerate(articles):
        if article.id == article_id:
            deleted_article = articles.pop(i)
            return deleted_article
    raise HTTPException(status_code=404, detail="Article not found")

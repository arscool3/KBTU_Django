from fastapi.testclient import TestClient
from main import app  
from pydantic import BaseModel

client = TestClient(app)

class TestArticle(BaseModel):
    id: int
    title: str
    author: str

def test_create_article():
    article_data = {"id": 1, "title": "Test Title", "author": "Test Author"}
    response = client.post("/articles", json=article_data)
    assert response.status_code == 200
    assert response.json() == article_data

def test_get_articles():
    response = client.get("/articles")
    assert response.status_code == 200

    assert len(response.json()) > 0

def test_update_article():
    article_data = {"id": 1, "title": "Updated Title", "author": "Updated Author"}
    response = client.get("/articles/1", json=article_data)
    assert response.status_code == 200
    assert response.json() == article_data

def test_delete_article():
    response = client.delete("/articles/1")
    assert response.status_code == 200


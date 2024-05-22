from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_books():
    response = client.get("/books/")
    assert response.status_code == 200


def test_create_book():
    response = client.post("/books/", json={"title": "Book Title", "author": "Author Name"})
    assert response.status_code == 200
    assert response.json()["title"] == "Book Title"

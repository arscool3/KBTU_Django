import pytest
import sqlalchemy
from sqlalchemy.orm import Session

from fastapi.testclient import TestClient
from main import app, get_db

from database import Base, engine
from schemas import CreateHotel

client = TestClient(app)

url = 'postgresql://postgres:postgres@localhost:5433/postgres_test'
engine = sqlalchemy.create_engine(url)
test_session = Session(engine)


def get_test_db():
    try:
        yield test_session
        test_session.commit()
    except:
        raise
    finally:
        test_session.close()


app.dependency_overrides[get_db] = get_test_db


@pytest.fixture
def test_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


def test_get_hotel(test_db):
    response = client.get("/hotels/{hotel_id}")
    assert response.json() == []


def test_add_hotel(test_db):
    response = client.post("/hotels",
    json={
        "name": "Test Hotel",
        "address": "123 Main Street",
        "stars": 5,
    })
    assert response.status_code == 200
    response = client.get("/hotels")
    assert response.json() == [{
        "name": "Test Hotel",
        "address": "123 Main Street",
        "stars": 5,
    }]


def test_get_room(test_db):
    response = client.get("/rooms/{room_id}")
    assert response.json() == []


def test_add_room(test_db):
    response = client.post("/rooms",
    json={
        "room_no": 1,
        "type": "double",
        "price": 45,
        "available": True,
        "hotel_id": 1,
    })
    assert response.status_code == 200
    response = client.get("/rooms")
    assert response.json() == [{
        "room_no": 1,
        "type": "double",
        "price": 45,
        "available": True,
        "hotel_id": 1,
    }]


def test_get_customer(test_db):
    response = client.get("/customers/{customer_id}")
    assert response.json() == []


def test_add_customer(test_db):
    response = client.post("/customers",
    json={
        "first_name": "Nursultan",
        "last_name": "Yerkenov",
        "phone_number": "87055521565",
    })
    assert response.status_code == 200
    response = client.get("/customers")
    assert response.json() == [{
        "first_name": "Nursultan",
        "last_name": "Yerkenov",
        "phone_number": "87055521565",
    }]


def test_get_reservation(test_db):
    response = client.get("/reservations/{reservation_id}")
    assert response.json() == []


def test_get_reviews(test_db):
    response = client.get("/reviews/{review_id}")
    assert response.json() == []


def test_get_payment(test_db):
    response = client.get("/payments/{payment_id}")
    assert response.json() == []
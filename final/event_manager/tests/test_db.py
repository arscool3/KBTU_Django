# test_database.py

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from ..event_manager.database.database import get_db, Base  # Import your module containing get_db() and Base

# Define a test database URL (can be different from your actual database)
TEST_DATABASE_URL = "postgresql://postgres:postgres@localhost/event_db"

# SQLAlchemy engine and session setup for testing
engine = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

@pytest.fixture(scope="module")
def test_session():
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()

def test_get_db(test_session):
    # Use the test_session fixture to simulate using the database session
    db = test_session

    # Call the get_db() function as it would be used in your application
    with get_db() as session:
        # Assert that the session returned by get_db() is the test_session
        assert session == db

    # Assert that the session is closed after exiting the context manager
    assert db.is_active is False  # Assuming `is_active` checks if session is closed

# Additional tests can be written to cover more scenarios

from database import SessionLocal

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
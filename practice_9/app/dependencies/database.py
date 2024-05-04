def get_db():
    db = "Database Connection"
    try:
        yield db
    finally:
        db = "Database Disconnected"

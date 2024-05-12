from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from . import database, models, schemas, token
import logging

class Logger:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            self.logger.info(f"Before executing {func.__name__}")
            result = func(*args, **kwargs)
            self.logger.info(f"After executing {func.__name__}")
            return result
        return wrapper
    
# Database Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Security Dependency
def get_current_user(db: Session = Depends(get_db), token: str = Depends(token.oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    user = token.verify_token(token)
    if user is None:
        raise credentials_exception
    return user
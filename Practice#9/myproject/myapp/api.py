from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from typing import Optional

app = FastAPI()

security = HTTPBearer()

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(token: HTTPAuthorizationCredentials = Depends(security)):
    if token.credentials != "secret-token":  
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )
    return {"user": "authorized"}

class CommonQueryParams(BaseModel):
    q: Optional[str] = None
    limit: int = 10
    offset: int = 0

def common_query_params(q: Optional[str] = None, limit: int = 10, offset: int = 0) -> CommonQueryParams:
    return CommonQueryParams(q=q, limit=limit, offset=offset)

@app.get("/items/")
def read_items(params: CommonQueryParams = Depends(common_query_params)):
    return {
        "query": params.q,
        "limit": params.limit,
        "offset": params.offset,
    }

@app.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        return {"id": user.id, "name": user.name}
    raise HTTPException(status_code=404, detail="User not found")

@app.get("/secure-data")
def secure_endpoint(user: dict = Depends(get_current_user)):
    return {"message": "This is secured data", "user": user}

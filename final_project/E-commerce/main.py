from typing import List
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session 
from auth.auth import create_access_token
from database import models
from database.db import engine, get_db
import entity
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from auth import auth


models.Base.metadata.create_all(bind=engine)
app = FastAPI()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/login')



@app.get("/user")
def read_root(db: Session = Depends(get_db)):
    user = db.query(models.User).first()
    return {"message": "Hello World!", "user": user.username}


@app.post("/login", response_model=entity.Token)
def login(details: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == details.username).first()

    if not user or details.password != user.password:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid username or password")
    
    access_token = create_access_token(data={"username": user.username, "user_id": user.user_id})
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/register", response_model=entity.User)
def register_user(user: entity.User, db: Session = Depends(get_db)):

    if db.query(models.User).filter(models.User.username == user.username).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists")

    last_user = db.query(models.User).order_by(models.User.user_id.desc()).first()
    next_user_id = (last_user.user_id + 1) if last_user else 1

    new_user = models.User(user_id=next_user_id, username=user.username, password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
    
@app.get("/me")
def read_users_me(current_user: models.User = Depends(auth.get_current_user)):
    return current_user


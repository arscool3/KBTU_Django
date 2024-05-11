# main.py
from fastapi import FastAPI, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from typing import List

from database import SessionLocal, engine
import models
import schemas
import crud
from crud import verify_token

app = FastAPI(swagger_ui_parameters={"syntaxHighlight": 'obsidian'})

# Dependency for getting the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create all tables in the database
models.Base.metadata.create_all(bind=engine)

# Seed data
@app.get("/seed")
async def seed_data(background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    background_tasks.add_task(crud.seed_data, db)
    return {"message": "Seeding started in the background"}

# Authorization function
def check_authorization(token: str = Depends(verify_token)):
    if not token:
        raise HTTPException(status_code=401, detail="Unauthorized")

# CRUD operations for Seed entity
@app.post("/seeds/", response_model=schemas.Seed)
def create_seed(seed: schemas.SeedCreate, db: Session = Depends(get_db), token: str = Depends(check_authorization)):
    return crud.create_seed(db, seed)

@app.get("/seeds/", response_model=List[schemas.Seed])
def read_seeds(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_seeds(db, skip=skip, limit=limit)

@app.get("/seeds/{seed_id}", response_model=schemas.Seed)
def read_seed(seed_id: int, db: Session = Depends(get_db)):
    return crud.get_seed(db, seed_id=seed_id)

@app.put("/seeds/{seed_id}", response_model=schemas.Seed)
def update_seed(seed_id: int, seed: schemas.SeedUpdate, db: Session = Depends(get_db), token: str = Depends(check_authorization)):
    return crud.update_seed(db, seed_id=seed_id, seed=seed)

@app.delete("/seeds/{seed_id}")
def delete_seed(seed_id: int, db: Session = Depends(get_db), token: str = Depends(check_authorization)):
    return crud.delete_seed(db, seed_id=seed_id)

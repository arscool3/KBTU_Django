import random
import asyncio
from fastapi import FastAPI, HTTPException, Depends, WebSocket
from sqlalchemy.orm import Session
import models
import schemas
import crud
import database

app = FastAPI()


@app.websocket("/webs")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")
        # await websocket.send_text(f"Message text was: {random.randint(1, 10)} ")
        # await asyncio.sleep(2)


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/employers/")
def get_employers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_employers(db, skip=skip, limit=limit)


@app.get("/employees/")
def get_employees(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_employees(db, skip=skip, limit=limit)


@app.get("/jobs/")
def get_jobs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_jobs(db, skip=skip, limit=limit)


@app.post("/employers/", response_model=schemas.Employer)
def create_employer(employer: schemas.EmployerCreate, db: Session = Depends(get_db)):
    return crud.create_employer(db=db, employer=employer)


@app.post("/employees/", response_model=schemas.Employee)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db=db, employee=employee)


@app.post("/jobs/", response_model=schemas.Job)
def create_job(job: schemas.JobCreate, db: Session = Depends(get_db)):
    return crud.create_job(db=db, job=job)

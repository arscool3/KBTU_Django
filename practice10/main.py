from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
import models
import schemas
import crud
import database

app = FastAPI()


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

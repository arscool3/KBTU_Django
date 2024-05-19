from typing import List

from sqlalchemy.orm import Session
import models
import schemas


def create_employer(db: Session, employer: schemas.EmployerCreate):
    db_employer = models.Employer(**employer.dict())
    db.add(db_employer)
    db.commit()
    db.refresh(db_employer)
    return db_employer


def create_employee(db: Session, employee: schemas.EmployeeCreate):
    db_employee = models.Employee(**employee.dict())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


def create_job(db: Session, job: schemas.JobCreate):
    db_job = models.Job(**job.dict())
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job


def get_employers(db: Session, skip: int = 0, limit: int = 10) -> List[models.Employer]:
    return db.query(models.Employer).offset(skip).limit(limit).all()


def get_employees(db: Session, skip: int = 0, limit: int = 10) -> List[models.Employee]:
    return db.query(models.Employee).offset(skip).limit(limit).all()


def get_jobs(db: Session, skip: int = 0, limit: int = 10) -> List[models.Job]:
    return db.query(models.Job).offset(skip).limit(limit).all()

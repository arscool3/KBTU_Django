from pydantic import BaseModel
from typing import List

from fastapi import FastAPI, HTTPException, Depends

from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from .models import *

async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)

app = FastAPI()

DATABASE_URL = "sqlite+aiosqlite:///./test.db"
Base = declarative_base()
engine = create_async_engine(DATABASE_URL, echo=True)

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.post("/departments/", response_model=DepartmentResponse)
async def create_department(department: DepartmentCreate, session: AsyncSession = Depends(async_session)):
    db_department = Department(name=department.name)
    session.add(db_department)
    await session.commit()
    await session.refresh(db_department)
    return db_department

@app.get("/departments/", response_model=List[DepartmentResponse])
async def read_departments(session: AsyncSession = Depends(async_session)):
    departments = await session.execute(Department.__table__.select())
    return departments.scalars().all()


# CRUD operations for Employee
@app.post("/employees/", response_model=EmployeeResponse)
async def create_employee(employee: EmployeeCreate, session: AsyncSession = Depends(async_session)):
    db_employee = Employee(name=employee.name, department_id=employee.department_id)
    session.add(db_employee)
    await session.commit()
    await session.refresh(db_employee)
    return db_employee

@app.get("/employees/", response_model=List[EmployeeResponse])
async def read_employees(session: AsyncSession = Depends(async_session)):
    employees = await session.execute(Employee.__table__.select())
    return employees.scalars().all()
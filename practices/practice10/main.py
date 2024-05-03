from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Student(BaseModel):
    id: int
    faculty_id: int
    fname: str
    lname: str
    email: str

class Faculty(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

class Teacher(BaseModel):
    id: int
    fname: str
    lname: str
    email: str

studets = []
faculties = []
teachers = []

@app.post("/students/", response_model=Student)
def create_student(student: Student):
    faculty_exists = any(f.id == student.faculty_id for f in faculties)
    if not faculty_exists:
        raise HTTPException(status_code=404, detail="Nonexistent faculty")

    students.append(student)
    return student

@app.get("/students/", response_model=List[Student])
def get_students():
    return students

@app.post("/teachers/", response_model=Teacher)
def create_teacher(teacher: Teacher):
    teachers.append(teacher)
    return teacher

@app.get("/teachers/", response_model=List[Teacher])
def get_teachers():
    return teachers

@app.post("/faculties/", response_model=Faculty)
def create_faculty(teacher: Faculty):
    faculties.append(faculty)
    return faculty

@app.get("/faculties/", response_model=List[Faculty])
def get_faculties():
    return faculties
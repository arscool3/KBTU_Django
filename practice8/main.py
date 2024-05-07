from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

students = []


class Student(BaseModel):
    name: str
    age: int
    grade: str
    address: str


@app.post("/students/")
def create_student(student: Student):
    students.append(student)
    return {"message": "Student created successfully", "student_details": student}


@app.get("/students/")
def get_students():
    return students


@app.get("/students/{student_id}")
def get_student(student_id: int):
    if student_id < 0 or student_id >= len(students):
        raise HTTPException(status_code=404, detail="Student not found")
    return students[student_id]


@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    if student_id < 0 or student_id >= len(students):
        raise HTTPException(status_code=404, detail="Student not found")
    students[student_id] = student
    return {"message": "Student updated successfully", "updated_student": student}


@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id < 0 or student_id >= len(students):
        raise HTTPException(status_code=404, detail="Student not found")
    deleted_student = students.pop(student_id)
    return {"message": "Student deleted successfully", "deleted_student": deleted_student}

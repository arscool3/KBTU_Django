from fastapi import FastAPI, HTTPException, WebSocket
from pydantic import BaseModel
from typing import List, Optional
from fastapi.responses import HTMLResponse

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

template = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""

@app.get("/")
async def get():
    return HTMLResponse(template)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")

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
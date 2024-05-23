from fastapi import FastAPI
import database
from routers import assignment_router, auth_router, course_router, instructor_router, student_router

database.Base.metadata.create_all(bind=database.engine)


app = FastAPI()

app.include_router(auth_router)
app.include_router(instructor_router)
app.include_router(course_router)
app.include_router(student_router)
app.include_router(assignment_router)
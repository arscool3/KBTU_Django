from fastapi import FastAPI
import database
from auth import router as auth_router
from auth import models as auth_models
from instructor import router as instructor_router
from instructor import models as instructor_models
from course import router as course_router
from student import router as student_router

auth_models.Base.metadata.create_all(bind=database.engine)
instructor_models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(auth_router.router)
app.include_router(instructor_router.router)
app.include_router(course_router.router)
app.include_router(student_router.router)
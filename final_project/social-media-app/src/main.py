from fastapi import FastAPI
from .database import Base, engine
from .api import auth_router, post_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Social Media App",
    description="Engine Behind Social Media App",
    version="0.1",
)

app.include_router(auth_router)
app.include_router(post_router)
print(app.routes)

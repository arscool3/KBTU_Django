import logging
from fastapi import FastAPI
from app.routers import user, video, comment, stream, token

from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

# Instrument the FastAPI app
Instrumentator().instrument(app).expose(app)

app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(video.router, prefix="/videos", tags=["videos"])
app.include_router(comment.router, prefix="/video", tags=["comments"])
app.include_router(stream.router, prefix="/streams", tags=["streams"])
app.include_router(token.router, prefix="/auth", tags=["auth"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

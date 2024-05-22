from fastapi import FastAPI
from app.routers.user import router

app = FastAPI()

app.include_router(router)
# app.include_router(auth.router, prefix="/auth", tags=["auth"])
# app.include_router(videos.router, prefix="/videos", tags=["videos"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

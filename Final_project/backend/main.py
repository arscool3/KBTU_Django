from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from fastapi.routing import APIRouter
from api.handlers import user_router, manager_router
from api.login_handler import login_router
from pydantic import BaseModel

app = FastAPI(title = "e-Gov")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

main_api_router = APIRouter()

main_api_router.include_router(user_router, prefix="/user", tags=["user"])
main_api_router.include_router(login_router, prefix="", tags=[""])
main_api_router.include_router(manager_router, prefix="/manager", tags=[""])



app.include_router(main_api_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port = 8000)


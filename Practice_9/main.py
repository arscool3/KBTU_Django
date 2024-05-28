from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
import datetime

app = FastAPI()


def get_current_user(token: str):
    if token != "secret_token":
        raise HTTPException(status_code=400, detail="Invalid token")
    return {"user_id": "123", "name": "John Doe"}


class Config:
    def __init__(self, environment: str, debug: bool):
        self.environment = environment
        self.debug = debug


def get_config():
    return Config(environment="production", debug=False)


def get_request_time():
    return datetime.datetime.now()


@app.get("/protected/")
def protected_route(user: dict = Depends(get_current_user)):
    return {"message": f"Welcome {user['name']}!"}


@app.get("/config/")
def show_config(config: Config = Depends(get_config)):
    return {"environment": config.environment, "debug": config.debug}


@app.get("/time/")
def current_time(request_time: datetime.datetime = Depends(get_request_time)):
    return {"request_time": request_time.isoformat()}
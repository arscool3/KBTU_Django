from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

class Token(BaseModel):
    token: str

def get_token_header(x_token: Optional[str] = None):
    if x_token is None or x_token != "q1w2e3r4":
        raise HTTPException(status_code=400, detail="Token is invalid")
    return x_token


@app.get("/items/")
def read_items(token: str = Depends(get_token_header)):
    return {"token": token}


class Security:
    def __init__(self, token: str = Depends(get_token_header)):
        self.token = token

@app.get("/secure-items/")
def read_secure_items(security: Security = Depends()):
    return {"token": security.token}


def common_params(q: Optional[str] = None, skip: int = 0, limit: int = 10):
    return {"q": q, "skip": skip, "limit": limit}

@app.get("/common-params/")
def get_common_params(commons: dict = Depends(common_params)):
    return commons
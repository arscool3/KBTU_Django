from fastapi import FastAPI, Depends, HTTPException, Request
import logging
from typing import Optional

app = FastAPI()

async def authMe(username: str, password: str) -> bool:
    return username == "Aibek" and password == "qwerty"

@app.get("/auth")
async def auth(username: str, password: str, authenticated: bool = Depends(authMe)):
    if not authenticated:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return {"message": "Successfully authenticated"}


def get_client_ip(request: Request):
    return request.client.host

@app.get("/checkIp")
async def check_ip_endpoint(remote_addr: str = Depends(get_client_ip)):
    if not remote_addr:
        raise HTTPException(status_code=403, detail="Access denied.")
    return {"message": f"IP address is allowed, {remote_addr}"}


logger = logging.getLogger(__name__)

async def log_request(url: Optional[str] = None):
    logger.info(f"Request to {url if url else 'unknown'}")

@app.get("/log")
async def log_endpoint(url: Optional[str] = None, _ = Depends(log_request)):
    return {"message": "Request logged"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
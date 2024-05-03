from fastapi import FastAPI, Depends, HTTPException
import logging
from typing import Optional

app = FastAPI()

# Example 1:
async def authenticate_user(username: str, password: str) -> bool:
    return username == "nursultan" and password == "password"

@app.get("/auth")
async def auth(username: str, password: str, authenticated: bool = Depends(authenticate_user)):
    if not authenticated:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return {"message": "Successfully authenticated"}


# Example 2:
async def check_ip(remote_addr: str) -> bool:
    return remote_addr == "127.0.0.1"

@app.get("/correct_ip")
async def check_ip_endpoint(remote_addr: str = Depends(check_ip)):
    if not remote_addr:
        raise HTTPException(status_code=403, detail="Access denied.")
    return {"message": "IP address is allowed"}


# Example 3:
logger = logging.getLogger(__name__)

async def log_request(url: Optional[str] = None):
    logger.info(f"Request to {url if url else 'unknown'}")

@app.get("/log")
async def log_endpoint(url: Optional[str] = None, _ = Depends(log_request)):
    return {"message": "Request logged"}

# uvicorn main:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
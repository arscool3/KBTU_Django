from fastapi import HTTPException

from fastapi import Header


def check_api_key(api_key: str = Header(...)):
    if api_key != "secret":
        raise HTTPException(status_code=401, detail="Invalid API key")

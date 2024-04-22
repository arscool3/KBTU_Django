from fastapi import Depends, FastAPI, HTTPException

app = FastAPI()


def get_query_token(token: str):
    if token != "KBTU_Django":
        raise HTTPException(status_code=400, detail="No auth token")
    return token


def get_token_header(token: str = Depends(get_query_token)):
    return token


@app.get("/token/")
async def get_token(token: str = Depends(get_token_header)):
    return {"token": token}

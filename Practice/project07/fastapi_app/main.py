from fastapi import FastAPI, Depends
from dependencies import get_token_header, get_query_token, CommonQueryParams

app = FastAPI()

@app.get("/items/")
async def read_items(commons: CommonQueryParams = Depends()):
    return {"q": commons.q, "skip": commons.skip, "limit": commons.limit}

@app.get("/items/header/")
async def read_items_header(token: str = Depends(get_token_header)):
    return {"token": token}

@app.get("/items/query/")
async def read_items_query(token: str = Depends(get_query_token)):
    return {"token": token}

from fastapi import FastAPI, Depends, HTTPException, Query, Header
import logging
from typing import Annotated, Optional

app = FastAPI()

async def pagination(offset: int = 0, limit: int = 10) -> tuple[int, int]:
    return (offset, limit)

@app.get("/paginated_list")
async def paginated_list(query: Annotated[(tuple[int, int], Depends(pagination))]):
    offset, limit = query
    return {"offset": offset, "limit": limit}



async def search_query(query: str = Query(None, title="Search Query")):
    if not query:
        return {"message": "No query provided"}
    return {"query": query}

@app.get("/search/")
async def search_results(result: Annotated[dict, Depends(search_query)]):
    return result


def get_token(authorization: str):
    if authorization != "token":
        raise HTTPException(status_code=401, detail="Unauthorized")
    return authorization

@app.get("/protected/")
async def protected_endpoint(token: Annotated[str, Depends(get_token)]):
    return {"token": token}

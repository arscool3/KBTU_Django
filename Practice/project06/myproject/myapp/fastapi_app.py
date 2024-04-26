from fastapi import FastAPI, Depends

app = FastAPI()

def get_query(limit: int = 10):
    return limit

@app.get("/items/")
async def read_items(limit: int = Depends(get_query)):
    return {"limit": limit}

@app.get("/users/")
async def read_users(limit: int = Depends(get_query)):
    return {"limit": limit}

@app.get("/products/")
async def read_products(limit: int = Depends(get_query)):
    return {"limit": limit}

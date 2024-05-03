from fastapi import FastAPI, Depends, HTTPException
from typing import Optional

app = FastAPI()

# Example1
def get_token_header(x_token: str = Depends(lambda x: x)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")
    return x_token

@app.get("/items/")
async def read_items(x: str = None, token: str = Depends(get_token_header)):
    return {"token": token, "x": x}

# Example2
class Dependency:
    def __init__(self, required_param: str):
        self.required_param = required_param

    def __call__(self, optional_param: str = None):
        return f"Required: {self.required_param}, Optional: {optional_param}"

dependency = Dependency(required_param="required_value")

@app.get("/dependency/")
async def test_dependency(dependency_result: str = Depends(dependency)):
    return {"dependency_result": dependency_result}

# Example3
async def get_query_parameter(q: Optional[str] = None):
    return {"q": q}

@app.get("/query/")
async def test_query_params(query_params: dict = Depends(get_query_parameter)):
    return query_params

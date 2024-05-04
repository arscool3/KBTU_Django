from fastapi import FastAPI, Depends

app = FastAPI()

# Example 1: Dependency as a function
async def get_token():
    return "fake_token"

@app.get("/example1/")
async def read_item(token: str = Depends(get_token)):
    return {"token": token}


# Example 2: Dependency as a class
class TokenGetter:
    def __init__(self):
        self.token = "fake_token"

    async def __call__(self):
        return self.token

token_getter = TokenGetter()

@app.get("/example2/")
async def read_item(token: str = Depends(token_getter)):
    return {"token": token}


# Example 3: Dependency with parameters
def get_token_from_header(x_token: str = Depends(lambda x: x.headers.get("x-token"))):
    return x_token

@app.get("/example3/")
async def read_item(token: str = Depends(get_token_from_header)):
    return {"token": token}

from fastapi import FastAPI, Depends

app = FastAPI()


def get_token_header(x_token: str = Depends(str)):
    return {"X-Token": x_token}


@app.get("/items/")
async def read_items(token: dict = Depends(get_token_header)):
    return {"token": token}


class TokenChecker:
    def __init__(self, token: str = Depends(str)):
        self.token = token

    def __call__(self):
        return {"token": self.token}


@app.get("/items2/")
async def read_items(token_data: dict = Depends(TokenChecker())):
    return token_data


async def common_parameters(q: str = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items3/")
async def read_items(q: str = None, params: dict = Depends(common_parameters)):
    return params

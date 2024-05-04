from fastapi import Depends, FastAPI, HTTPException

app = FastAPI()


def get_user_agent(user_agent: str = Depends(lambda x: x.headers["user-agent"])):
    return user_agent

@app.get("/user-agent/")
async def read_user_agent(user_agent: str = Depends(get_user_agent)):
    return {"User-Agent": user_agent}


class FakeDB:
    def __init__(self):
        self.items = {"foo": "The Foo Wrestler", "bar": "The Bar Fighter"}

    def get_item(self, item_id: str):
        if item_id in self.items:
            return self.items[item_id]
        return None

fake_db = FakeDB()

def get_db():
    return fake_db

@app.get("/items/{item_id}")
async def read_item(item_id: str, db: FakeDB = Depends(get_db)):
    item = db.get_item(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": item}



async def common_parameters(q: str = None, skip: int = 0, limit: int = 10):
    return {"q": q, "skip": skip, "limit": limit}

@app.get("/items/")
async def read_items(params: dict = Depends(common_parameters)):
    return params
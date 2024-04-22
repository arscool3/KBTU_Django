from fastapi import FastAPI, Depends

app = FastAPI()


# 1
def get_current_user():
    return {"username": "Dias", "id": 1}


# 2
def get_current_item(user: dict = Depends(get_current_user)):
    return {"item_id": 1, "owner_id": user["id"]}


# 3
def process_item(item: dict = Depends(get_current_item)):
    return f"Processing item {item['item_id']} by user {item['owner_id']}"


@app.get("/")
async def read_item(result: str = Depends(process_item)):
    return {"result": result}

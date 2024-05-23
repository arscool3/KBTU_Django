from fastapi import FastAPI, Depends

app = FastAPI()


def get_user():
    return "Sala"

def get_item():
    return "Laptop"

def get_order(user: str = Depends(get_user), item: str = Depends(get_item)):
    return {"user": user, "item" : item, "status": "done"}



@app.get("/order")
def get_order(order: dict = Depends(get_order)):
    return order

from fastapi import Depends, FastAPI

app = FastAPI()

def get_user_by_id(user_id: int):
    return {"user_id": user_id}

@app.get("/users/{user_id}")
def get_user(user: dict = Depends(get_user_by_id)):
    return user
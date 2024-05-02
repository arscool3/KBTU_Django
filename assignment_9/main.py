from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from starlette import status

app = FastAPI()

class User(BaseModel):
    username: str
    is_admin: bool

def get_current_user():
    user = User(username='Darkhan', is_admin=True)
    return user

def require_admin(user: User = Depends(get_current_user)):
    if not user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
        )
    return user

@app.get("/user")
def get_profile(user: User = Depends(require_admin)):
    return {'message': f'Welcome {user.username}'}

#uvicorn main:app --reload

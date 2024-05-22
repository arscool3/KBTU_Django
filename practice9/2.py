from fastapi import Depends, FastAPI, Request

app = FastAPI()

def get_user_agent(request: Request):
    return request.headers.get("user-agent")

@app.get("/user-agent")
def get_user_agent_route(user_agent: str = Depends(get_user_agent)):
    return {"user_agent": user_agent}
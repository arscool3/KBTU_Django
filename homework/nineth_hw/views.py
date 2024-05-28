from fastapi import FastAPI, Depends

app = FastAPI()

# Example 1: Dependency Injection using functions
def get_token_header(x_token: str = Depends()):
    return {"X-Token": x_token}

@app.get("/")
async def read_root(token_header: dict = Depends(get_token_header)):
    return {"X-Token": token_header}

# Example 2: Dependency Injection using classes
class UserAgent:
    def __init__(self, user_agent: str = "generic"):
        self.user_agent = user_agent

    def __call__(self, x_user_agent: str = Depends()):
        return {"X-User-Agent": f"{self.user_agent} - {x_user_agent}"}

@app.get("/user-agent")
async def read_user_agent(user_agent: dict = Depends(UserAgent())):
    return user_agent

# Example 3: Dependency Injection with nested dependencies
async def get_db_connection():
    db_connection = "Fake DB Connection"
    yield db_connection
    print("Closing DB Connection")
    # Close database connection here if necessary

async def get_current_user(db: str = Depends(get_db_connection)):
    user = "John Doe"
    return user

async def get_current_user_info(user: str = Depends(get_current_user), token: str = Depends()):
    return {"user": user, "token": token}

@app.get("/user-info")
async def read_user_info(info: dict = Depends(get_current_user_info)):
    return info

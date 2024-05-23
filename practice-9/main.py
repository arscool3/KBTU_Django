from fastapi import FastAPI, Depends, HTTPException, status

app = FastAPI()

# Example 1: Simple Dependency for Providing a Fixed Response
def get_fixed_response():
    return {"message": "Hello from a dependency!"}

@app.get("/example1/")
async def show_message(response: dict = Depends(get_fixed_response)):
    return response

# Example 2: Dependency with State (A Counter)
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return {"count": self.count}

def get_counter():
    counter = Counter()
    return counter

@app.get("/example2/")
async def count_visits(counter: Counter = Depends(get_counter)):
    return counter.increment()

# Example 3: Dependency for Basic Authorization Check
def check_authorization(user_id: int):
    if user_id != 1:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Unauthorized")
    return {"status": "Authorized"}

@app.get("/example3/{user_id}")
async def access_protected_resource(auth: dict = Depends(check_authorization)):
    return auth


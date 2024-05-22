from fastapi import Depends, FastAPI

app = FastAPI()

def get_db_connection():
    # Connect to the database
    return "db_connection"

def get_user_data(db_connection: str = Depends(get_db_connection)):
    # Fetch user data using the database connection
    return {"user_id": 123, "username": "example"}

@app.get("/user")
def get_user_route(user_data: dict = Depends(get_user_data)):
    return user_data
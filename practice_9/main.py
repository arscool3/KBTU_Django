# Practice #9

# Fastapi Application
# With 3 examples of Dependency Injection

import asyncpg
from fastapi import FastAPI, Depends

app = FastAPI()

# PostgreSQL database settings
POSTGRES_USER = 'postgres'
POSTGRES_PASSWORD = 'postgres'
POSTGRES_DB = 'postgres'
POSTGRES_HOST = 'localhost'
POSTGRES_PORT = '5432'

# Example 1: Dependency Injection using a simple function
async def get_db_connection():
    conn = await asyncpg.connect(
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        database=POSTGRES_DB,
        host=POSTGRES_HOST,
        port=POSTGRES_PORT
    )
    return conn

@app.get("/sample1/")
async def example1(db: asyncpg.Connection = Depends(get_db_connection)):
    return {"message": f"Using Dependency Injection - DB Connection: {db}"}

# Example 2: Dependency Injection using a class
class DBConnection:
    def __init__(self):
        self.connection = "Fake DB Connection"

def get_db():
    db = DBConnection()
    return db

@app.get("/sample2/")
async def example2(db: DBConnection = Depends(get_db)):
    return {"message": f"Using Dependency Injection - DB Connection: {db.connection}"}

# Example 3: Dependency Injection using a class method
class AuthService:
    def __init__(self):
        self.token = "Fake Auth Token"

    def get_token(self):
        return self.token

def get_auth_token(auth_service: AuthService = Depends(AuthService)):
    token = auth_service.get_token()
    return token


@app.get("/sample3/")
async def example3(token: str = Depends(get_auth_token)):
    return {"message": f"Using Dependency Injection - Auth Token: {token}"}

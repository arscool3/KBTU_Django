from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import redis

app = FastAPI()

redis_client = redis.Redis(host='localhost', port=6379)

class Test(BaseModel):
    test: str

@app.post("/tests/")
async def create_test(test: Test):
    redis_client.set('test_data', test.test)
    return {"message": "Test created successfully"}

@app.get("/tests/")
async def read_test():
    test_data = redis_client.get('test_data')
    if not test_data:
        raise HTTPException(status_code=404, detail="Test data not found")
    return {"test": test_data.decode('utf-8')}

@app.put("/tests/")
async def update_test(test: Test):
    redis_client.set('test_data', test.test)
    return {"message": "Test updated successfully"}

@app.delete("/tests/")
async def delete_test():
    redis_client.delete('test_data')
    return {"message": "Test deleted successfully"}

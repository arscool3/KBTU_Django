from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Test(BaseModel):
    id: int
    test: str

test_data = []

@app.post("/tests/")
def create_test(item: Test):
    test_data.append(item)
    return {"message": "Test created successfully"}

# Endpoint to get all tests
@app.get("/tests/")
def get_tests():
    return test_data

@app.get("/tests/{test_id}")
def get_test(test_id: int):
    try:
        return test_data[test_id]
    except IndexError:
        raise HTTPException(status_code=404, detail="Test not found")

@app.put("/tests/{test_id}")
def update_test(test_id: int, item: Test):
    try:
        test_data[test_id] = item
        return {"message": "Test updated successfully"}
    except IndexError:
        raise HTTPException(status_code=404, detail="Test not found")

@app.delete("/tests/{test_id}")
async def delete_test(test_id: int):
    try:
        del test_data[test_id]
        return {"message": "Test deleted successfully"}
    except IndexError:
        raise HTTPException(status_code=404, detail="Test not found")
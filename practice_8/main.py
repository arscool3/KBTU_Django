from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Test(BaseModel):
    test: str

tests = []

@app.put("/tests/{test_id}")
def update_test(test_id: int, test: Test):
    if test_id >= len(tests):
        raise HTTPException(status_code=404, detail="Test not found")
    tests[test_id] = test
    return {"message": "Test updated successfully"}

@app.post("/tests/")
def create_test(test: Test):
    tests.append(test)
    return {"message": "Test created successfully"}

@app.delete("/tests/{test_id}")
def delete_test(test_id: int):
    if test_id >= len(tests):
        raise HTTPException(status_code=404, detail="Test not found")
    del tests[test_id]
    return {"message": "Test deleted successfully"}

@app.get("/tests/{test_id}")
def get_test(test_id: int):
    if test_id >= len(tests):
        raise HTTPException(status_code=404, detail="Test not found")
    return tests[test_id]

@app.get("/tests")
def get_tests():
    return tests

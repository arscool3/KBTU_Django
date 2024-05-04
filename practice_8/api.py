from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Test(BaseModel):
    id: int
    name: str
    description: str

tests_db: List[Test] = []


@app.get("/tests/", response_model=List[Test])
def get_tests():
    return tests_db

@app.post("/tests/", response_model=Test, status_code=201)
def create_test(test: Test):
    tests_db.append(test)
    return test

@app.get("/tests/{test_id}", response_model=Test)
def get_test(test_id: int = Path(..., title="ID of the test to extract", ge=0)):
    for test in tests_db:
        if test.id == test_id:
            return test
    raise HTTPException(status_code=404, detail="Test not found")

@app.put("/tests/{test_id}", response_model=Test)
def update_test(test_id: int, test: Test):
    for index, existing_test in enumerate(tests_db):
        if existing_test.id == test_id:
            tests_db[index] = test
            return test
    raise HTTPException(status_code=404, detail="Test not found")

@app.delete("/tests/{test_id}")
def delete_test(test_id: int):
    for index, existing_test in enumerate(tests_db):
        if existing_test.id == test_id:
            deleted_test = tests_db.pop(index)
            return {"message": f"Test with ID {test_id} was deleted"}
    raise HTTPException(status_code=404, detail="Test not found")
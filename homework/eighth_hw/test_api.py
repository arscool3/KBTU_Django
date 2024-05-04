from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

class Test(BaseModel):
    test: str

# In-memory database
db: Dict[int, Test] = {}

# Endpoint to create a test
@app.post("/tests/")
def create_test(test: Test):
    test_id = len(db) + 1
    db[test_id] = test
    return {"id": test_id, "test": test}

# Endpoint to retrieve a test by id
@app.get("/tests/{test_id}")
def read_test(test_id: int):
    if test_id not in db:
        raise HTTPException(status_code=404, detail="Test not found")
    return db[test_id]

# Endpoint to update a test by id
@app.put("/tests/{test_id}")
def update_test(test_id: int, test: Test):
    if test_id not in db:
        raise HTTPException(status_code=404, detail="Test not found")
    db[test_id] = test
    return {"id": test_id, "test": test}

# Endpoint to delete a test by id
@app.delete("/tests/{test_id}")
def delete_test(test_id: int):
    if test_id not in db:
        raise HTTPException(status_code=404, detail="Test not found")
    del db[test_id]
    return {"message": "Test deleted"}

# Define test cases
tests = [
    {"test": "First test"},
    {"test": "Second test"},
]

# Test class
class TestAPI:

    @staticmethod
    def test_create_test():
        response = app.post("/tests/", json=tests[0])
        assert response.status_code == 200
        assert "id" in response.json()
        assert response.json()["test"] == tests[0]["test"]

    @staticmethod
    def test_read_test():
        response = app.get("/tests/1")
        assert response.status_code == 200
        assert response.json()["test"] == tests[0]["test"]

    @staticmethod
    def test_update_test():
        updated_test = {"test": "Updated test"}
        response = app.put("/tests/1", json=updated_test)
        assert response.status_code == 200
        assert response.json()["test"] == updated_test["test"]

    @staticmethod
    def test_delete_test():
        response = app.delete("/tests/1")
        assert response.status_code == 200
        assert response.json()["message"] == "Test deleted"

# Run the tests
TestAPI.test_create_test()
TestAPI.test_read_test()
TestAPI.test_update_test()
TestAPI.test_delete_test()

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

tests = {}


class Test(BaseModel):
    test_id: int
    test: str


@app.get("/tests/", response_model=list[Test])
def get_all_tests():
    return list(tests.values())


@app.get("/tests/{test_id}", response_model=Test)
def get_test(test_id: int):
    if test_id not in tests:
        raise HTTPException(status_code=404, detail="Test not found")
    return tests[test_id]


@app.post("/tests/", status_code=201)
def create_test(test: Test):
    current_max_id = 0
    if tests:
        current_max_id = max(tests.keys())
    test_id = current_max_id + 1
    test.test_id = test_id
    tests[test_id] = test
    return test


@app.put("/tests/{test_id}")
def update_test(test_id: int, test: Test):
    if test_id not in tests:
        raise HTTPException(status_code=404, detail="Test not found")
    tests[test_id] = test
    return {"message": "Test updated"}


@app.delete("/tests/{test_id}", status_code=204)
def delete_test(test_id: int):
    if test_id not in tests:
        raise HTTPException(status_code=404, detail="Test not found")
    del tests[test_id]
    return None

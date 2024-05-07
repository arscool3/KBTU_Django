from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Test(BaseModel):
    test: str


tests = ['xaxa']


@app.post("/tests/")
def create_test(test: Test):
    tests.append(test)
    return test


@app.get("/tests/")
def read_tests():
    return tests


@app.get("/tests/{test_id}")
def read_test(test_id: int):
    if test_id < 0 or test_id >= len(tests):
        raise HTTPException(status_code=404, detail="Test not found")
    return tests[test_id]


@app.put("/tests/{test_id}")
def update_test(test_id: int, test: Test):
    if test_id < 0 or test_id >= len(tests):
        raise HTTPException(status_code=404, detail="Test not found")
    tests[test_id] = test
    return test


@app.delete("/tests/{test_id}")
def delete_test(test_id: int):
    if test_id < 0 or test_id >= len(tests):
        raise HTTPException(status_code=404, detail="Test not found")
    deleted_test = tests.pop(test_id)
    return {"message": "Test deleted", "deleted_test": deleted_test}

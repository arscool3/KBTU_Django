from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Test(BaseModel):
    id: int
    test: str

tests = []


@app.post("/tests/")
def create_test(test: Test):
    tests.append(test)
    return {"status": "Test created"}


@app.get("/tests/")
def read_tests():
    return tests


@app.get("/tests/{test_id}")
def read_test(test_id: int):
    if test_id < len(tests):
        return tests[test_id]
    else:
        raise HTTPException(status_code=404, detail="Test not found")


@app.put("/tests/{test_id}")
def update_test(test_id: int, test: Test):
    if test_id < len(tests):
        tests[test_id] = test
        return {"status": "Test updated"}
    else:
        raise HTTPException(status_code=404, detail="Test not found")


@app.delete("/tests/{test_id}")
def delete_test(test_id: int):
    if test_id < len(tests):
        del tests[test_id]
        return {"status": "Test deleted"}
    else:
        raise HTTPException(status_code=404, detail="Test not found")

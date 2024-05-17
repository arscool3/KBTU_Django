from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Test(BaseModel):
    test: str


tests = []


@app.post("/tests/")
async def create_test(test: Test):
    tests.append(test)
    return test


@app.get("/tests/")
async def read_tests():
    return tests


@app.get("/tests/{test_id}")
async def read_test(test_id: int):
    if test_id < len(tests):
        return tests[test_id]
    else:
        raise HTTPException(status_code=404, detail="Test not found")


@app.put("/tests/{test_id}")
async def update_test(test_id: int, test: Test):
    if test_id < len(tests):
        tests[test_id] = test
        return {"message": "Test updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Test not found")


@app.delete("/tests/{test_id}")
async def delete_test(test_id: int):
    if test_id < len(tests):
        deleted_test = tests.pop(test_id)
        return {"message": "Test deleted successfully", "deleted_test": deleted_test}
    else:
        raise HTTPException(status_code=404, detail="Test not found")

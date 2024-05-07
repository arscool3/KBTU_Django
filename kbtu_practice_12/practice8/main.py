from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Test(BaseModel):
    test: str

tests = []

@app.post("/tests/", response_model=Test)
async def create_test(item: Test):
    tests.append(item)
    return item

@app.get("/tests/", response_model=list[Test])
async def read_tests():
    return tests

@app.put("/tests/{test_id}", response_model=Test)
async def update_test(test_id: int, item: Test):
    if test_id >= len(tests):
        raise HTTPException(status_code=404, detail="Test not found")
    tests[test_id] = item
    return item

@app.delete("/tests/{test_id}")
async def delete_test(test_id: int):
    if test_id >= len(tests):
        raise HTTPException(status_code=404, detail="Test not found")
    del tests[test_id]
    return {"message": "Test deleted"}

tests.append(Test(test="First test"))
tests.append(Test(test="Second test"))
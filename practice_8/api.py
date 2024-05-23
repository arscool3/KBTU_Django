from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel

app = FastAPI()


tests = []
class Test(BaseModel):
    test_name: str


@app.get("/")
def get_all_tests() ->dict:
    if len(tests) < 1:
        return {"tests": "none"}
    else:
        return {"tests": tests}

@app.get("/{test_id}")
def get_test_by_id(test_id: int) -> dict:
    if test_id not in tests:
        raise HTTPException(status_code=404, detail="Test not found")
    return {"test_id": test_id, "value": tests[test_id]}

@app.post("/")
def add_test(test: Test) -> dict:
    tests.append(test)
    return {f"test {len(tests) - 1} created:": f"test name: {test.test_name}"}

@app.put("/{test_id}")
def update_test(test_id: int, test: Test) -> dict:
    tests[test_id] = test
    return {f"test {test_id} was updated": f"new value is {test.test_name}"}

@app.delete("/{test_id}")
async def delete_test(test_id: int) -> dict:
    if test_id >= len(tests):
        raise HTTPException(status_code=404, detail="Test not found")
    tests.pop(test_id)
    return {"message": f"Test with ID {test_id} has been deleted"}

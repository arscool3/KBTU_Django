from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

tests = []
class TestData(BaseModel):
    x: int

@app.post("/number/")
async def create_test(test_data: TestData):
    tests.append(test_data)
    return {"message": "number created successfully"}

@app.get("/number/")
async def get_tests():
    return tests

@app.get("/number/{number_id}")
async def get_test(test_id: int):
    try:
        return tests[test_id]
    except:
        raise HTTPException(status_code=404, detail="NOT FOUND!")

@app.put("/number/{number_id}")
async def update_test(test_id: int, test_data: TestData):
    if test_id < 0 or test_id >= len(tests):
        raise HTTPException(status_code=404, detail="number not found")
    tests[test_id] = test_data
    return {"message": "number updated successfully"}

@app.delete("/number/{number_id}")
async def delete_test(test_id: int):
    try:
        del tests[test_id]
    except:
        raise HTTPException(status_code=404, detail="number not found")
    return {"message": "number deleted successfully"}
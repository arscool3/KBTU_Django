from fastapi import FastAPI
from tasks import process_data_task, analyze_data_task

app = FastAPI()

@app.post("/process_data")
async def process_data_endpoint(data: str):
    process_data_task.send(data)
    return {"message": "Data processing started."}

@app.post("/analyze_data")
async def analyze_data_endpoint(data: str):
    analyze_data_task.send(data)
    return {"message": "Data analysis started."}

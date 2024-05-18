import dramatiq
from fastapi import FastAPI
from dramatiq.brokers.redis import RedisBroker
from dramatiq.results import Results
from dramatiq.results.backends.redis import RedisBackend
from pydantic import BaseModel

def crime_service(iin: str) -> bool:
    return True

def psycho_service(iin: str) -> bool:
    return False

def drugs_service(iin: str) -> bool:
    return True


result_backend = RedisBackend()
redis_broker = RedisBroker()
redis_broker.add_middleware(Results(backend=result_backend))
dramatiq.set_broker(redis_broker)

# Dramatiq actor
@dramatiq.actor(store_results=True)
def add_employee_task(iin: str):
    print('started')
    result = crime_service(iin) & drugs_service(iin) & psycho_service(iin)
    print('ended', result)
    return result

app = FastAPI()

class EmployeeData(BaseModel):
    iin: str

@app.post("/check_employee/")
def check_employee(data: EmployeeData):
    job = add_employee_task.send(data.iin)
    return {"message": "Check initiated", "job_id": job.message_id}

@app.get("/check_result/{job_id}")
def check_result(job_id: str):
    job = dramatiq.get_broker().get_result_backend().get_result(job_id, block=False)
    if job is None:
        return {"message": "Job still processing or does not exist."}
    return {"message": "Job completed", "result": job}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


jobs = []


class Job(BaseModel):
    title: str
    description: str
    company: str
    location: str


@app.post("/jobs/")
def create_job(job: Job):
    jobs.append(job)
    return {"message": "Job created successfully", "job_details": job}


@app.get("/jobs/")
def get_jobs():
    return jobs


@app.get("/jobs/{job_id}")
def get_job(job_id: int):
    if job_id < 0 or job_id >= len(jobs):
        raise HTTPException(status_code=404, detail="Job not found")
    return jobs[job_id]


@app.put("/jobs/{job_id}")
def update_job(job_id: int, job: Job):
    if job_id < 0 or job_id >= len(jobs):
        raise HTTPException(status_code=404, detail="Job not found")
    jobs[job_id] = job
    return {"message": "Job updated successfully", "updated_job": job}


@app.delete("/jobs/{job_id}")
def delete_job(job_id: int):
    if job_id < 0 or job_id >= len(jobs):
        raise HTTPException(status_code=404, detail="Job not found")
    deleted_job = jobs.pop(job_id)
    return {"message": "Job deleted successfully", "deleted_job": deleted_job}

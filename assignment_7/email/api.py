from fastapi import FastAPI, HTTPException
from dramatiq.results.errors import ResultMissing

from pydantic import BaseModel
from tasks import send_email_task, result_backend

app = FastAPI()


class EmailRequest(BaseModel):
    to: str
    subject: str
    body: str

@app.post("/send_email")
def send_email(email_content: EmailRequest) -> dict:
    """API endpoint to send an email."""
    task = send_email_task.send(email_content.to, email_content.subject, email_content.body)
    return {'task_id': task.message_id}


@app.get("/get_status")
def get_status(message_id: str):
    """API endpoint to get the status of an email send operation."""
    try:
        result = result_backend.get_result(message_id)
        if result is None:
            return {"status": "pending"}
        return {"status": "completed", "result": result}
    except ResultMissing:
        return {"status": "not found"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

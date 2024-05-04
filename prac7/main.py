# main.py
from fastapi import FastAPI
from tasks import send_email_task

app = FastAPI()

@app.post("/send-email/")
async def send_email(recipient: str, subject: str, message: str):
    send_email_task.send(recipient, subject, message)
    return {"message": "Email sending task queued"}


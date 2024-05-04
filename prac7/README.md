### How to start
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
dramatiq tasks
curl -X POST "http://localhost:8000/send-email/" -H "Content-Type: application/json" -d '{"recipient": "example@example.com", "subject": "Test Subject", "message": "Hello, this is a test email"}'

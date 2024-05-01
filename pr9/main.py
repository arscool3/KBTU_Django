from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()


class Database:
    def __init__(self, db_connection):
        self.db_connection = db_connection


create_db_connection = ""


@app.get("/constructor")
async def read_root(db: Database = Depends(create_db_connection)):
    return {"message": f"Database connection: {db.db_connection}"}


# Example 2: Function di
class EmailService:
    def send(self, subject: str, message: str):
        print(f"Sending email with subject '{subject}' and message '{message}'")


def get_email_service() -> EmailService:
    return EmailService()


def send_email(email_service, subject, message):
    email_service.send(subject, message)


@app.get("/")
async def read_root(email_service=Depends(get_email_service)):
    send_email(email_service, "Subject", "Message")
    return {"message": "Email sent successfully"}


# Example 3: authorization and authentication di
async def verify_token(token: str) -> dict:

    if token != "valid_token":
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"user_id": 123, "username": "john_doe", "roles": ["admin"]}


async def check_permissions(user_info: dict) -> dict:
    if "admin" not in user_info.get("roles", []):
        raise HTTPException(status_code=403, detail="Insufficient permissions")
    return user_info


@app.get("/protected/")
async def protected_route(token: str = Depends(verify_token), user_info: dict = Depends(check_permissions)):

    return {"message": "Access granted!"}

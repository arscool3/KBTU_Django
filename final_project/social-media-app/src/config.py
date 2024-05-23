import os

from dotenv import load_dotenv

load_dotenv(".env")

SMTP_USER = os.environ.get("SMTP_USER")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD")
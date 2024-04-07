import time
import random

def send_email(to: str, subject: str, body: str):
    print(f"Sending email to {to} with subject '{subject}'")
    time.sleep(random.randint(1, 5))
    print("Email sent.")
    return True

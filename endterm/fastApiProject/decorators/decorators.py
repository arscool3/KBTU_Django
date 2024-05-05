import uuid
from datetime import datetime
from functools import wraps
from typing import Callable

from task import celery_app, log_to_file, reserve_ticket

def get_current_time():
    return datetime.now()

def generate_log_id():
    return uuid.uuid4()

def create_log(filename: str, username: str, method: str, message: str):
    log_to_file.delay(f"{filename}", f"LOG_ID: {generate_log_id()} ---- "
                                                 f"TIME: {get_current_time()} ---- "
                                                 f"USER: {username} ---- "
                                                 f"OPERATION: {method} ---- "
                                                 f"MESSAGE: {message}")
def log_action_start(filename: str, message: str):
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            request = kwargs.get('request')
            username = kwargs.get('username')
            create_log(filename, username, request.method, message)
            return func(*args, **kwargs)
        return wrapper
    return decorator

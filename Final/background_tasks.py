# app/background_tasks.py

from typing import Any, Dict

from dramatiq import actor
from dramatiq.middleware import Middleware
from dramatiq.results import Result

from .models import Seed


class CustomMiddleware(Middleware):
    def after_process_message(self, broker, message, *, result: Result = None, exception: Exception = None):
        # Implement any custom logic here
        pass


@actor
def process_seed(seed_id: int):
    seed = Seed.get(id=seed_id)
    # Do something with the seed


# Define other background tasks here

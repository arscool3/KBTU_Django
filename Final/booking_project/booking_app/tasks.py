import dramatiq

@dramatiq.actor
def example_task():
    print("Hello, world!")
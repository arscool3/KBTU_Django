import dramatiq
from tasks import archive_past_events

# Register the task with dramatiq
dramatiq.set_broker(dramatiq.get_broker())  # Use the default in-memory broker

if __name__ == "__main__":
    # Start the dramatiq worker to process tasks
    dramatiq.Worker().run()

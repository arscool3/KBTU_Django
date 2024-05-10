import dramatiq


@dramatiq.actor
def process_payment():
    print("Processing payment")

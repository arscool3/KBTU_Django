import dramatiq

@dramatiq.actor
def print_message_task(message):
  print(message)
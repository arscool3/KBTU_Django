from dramatiq import actor

class BackgroundTasks:
    def start(self):
        print("Background tasks are started")

    def stop(self):
        print("Background tasks are stopped")

@actor
def add_book(title):
    print(f"Adding book {title}")



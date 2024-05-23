from locust import HttpUser, task, between, events

class FastAPIUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def get_comments(self):
        self.client.get("/video/1/comments")

    @task
    def create_comment(self):
        self.client.post("/video/1/comments", json={"content": "Great video"})

@events.request.add_listener
def log_request(request_type, name, response_time, response_length, response, context, exception, **kwargs):
    if exception:
        print(f"Request failed: {exception}")

@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    print("Test is starting")

@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    print("Test is stopping")

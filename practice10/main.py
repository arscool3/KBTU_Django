
import logging
from fastapi import FastAPI


app = FastAPI()

#example for loggin
class SomeClass:
    def __init__(self, logger=None):
        self.logger = logger or logging.getLogger(__name__)

    def some_method(self):
        self.logger.info("This is an informational message")

logger = logging.getLogger(__name__)
obj = SomeClass(logger)
obj.some_method()

@app.get("/")
def root():
    obj.some_method()
    return {"message": "Hello, World!"}

#example for configuration
class DatabaseConnection:
    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password

config = {
    "host": "localhost",
    "port": 5432,
    "username": "user",
    "password": "password"
}
db_connection = DatabaseConnection(**config)

@app.get("/database")
def root():
    return {"message": "Database connection established"}

#example for mocking dependensies in testing
class Dependency:
    def some_method(self):
        return "Dependency's method called"

class Client:
    def __init__(self, dependency):
        self.dependency = dependency

    def do_something(self):
        return self.dependency.some_method()

dependency = Dependency()

@app.get("/testing")
def root():
    client = Client(dependency)
    return {"message": client.do_something()}


from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def greeting():
    return {'greeting': 'Hello World'}
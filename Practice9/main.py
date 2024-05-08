from fastapi import Depends, FastAPI
import time
import random
import requests
from datetime import datetime

app = FastAPI()

def current_temperature():
    time.sleep(1)
    return random.randint(-10, 40)

@app.get("/clouth_advise/")
def clouth_advise(temperature: dict = Depends(current_temperature)):
    if temperature < 10:
        return 'Wear warmer'
    else:
        return 'Wear hoodie'

def get_traffic_level():
    response = requests.get("https://jam.api.2gis.com/almaty/meta/score/0/")
    traffic_level = int(response.text[1:-1])
    return traffic_level

@app.get("/traffic_jam_info/")
def traffic_jam_info(traffic_level: dict = Depends(get_traffic_level)):
    if traffic_level > 8:
        return 'Stay home'
    else:
        return 'Here we go'

def get_days_until_exam():
    return (datetime.strptime('2024-06-01', '%Y-%m-%d') - datetime.now()).days

@app.get("/prepare_exams/")
def prepare_exams(days_until_exam: dict = Depends(get_days_until_exam)):
    if days_until_exam > 30 or days_until_exam < 0:
        return 'Chill'
    elif days_until_exam > 0:
        return 'Prepare'
    elif days_until_exam == 0:
        return 'Keep calm'

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)


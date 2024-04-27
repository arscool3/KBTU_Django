import requests

url = 'http://127.0.0.1:8000/aircrafts/1'

data = {
    "id": 10,
    "aircraft_code": "A320",
    "full_name": "Airbus 320",
    "short_name": "A320",
    "built_date": "2020-01-01",
    "full_capacity": 180,
    "economy_capacity": 180,
    "business_capacity": 0,
    "owner_airline": 2
}

response = requests.delete(url)

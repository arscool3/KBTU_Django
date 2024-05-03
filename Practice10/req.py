import requests

url = 'http://127.0.0.1:8000/clients/'

data = {
    "name": "John",
    "surname": "Doe",
    "email": "john.doe@example.com",
    "phone": "123-456-7890"
}

response = requests.post(url, json=data)

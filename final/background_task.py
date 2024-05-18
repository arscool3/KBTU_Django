import requests

PAYMENT_SERVICE_URL = "url"
API_KEY = "api_key"


def process_payment_with_service(payment_id, amount):

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    payload = {
        "payment_id": payment_id,
        "amount": amount,
        "currency": "USD"
    }
    try:
        response = requests.post(PAYMENT_SERVICE_URL, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Failed to process payment: {e}")
        return None
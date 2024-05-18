from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup
import json
import httpx
import time

def retry(*exceptions, attempts:int=10, delay:int=1):
    if attempts <= 0: raise Exception("Number of attempts are negative or 0")
    if delay < 0: raise Exception("Delay ")

    def decorator(func):
        def wrapper(*args, **kwargs):
            num_attempts = attempts
            current_delay = delay
            while num_attempts > 0:
                try:
                    result = func(*args, **kwargs)
                    return result
                except exceptions as e:
                    print(f"{attempts - num_attempts + 1}: Exception {type(e).__name__}, {e}")
                    num_attempts -= 1
                    if num_attempts == 0:
                        raise e
                    time.sleep(current_delay)
                    if(num_attempts==1):
                        return None

        return wrapper
    return decorator

load_dotenv()


def get_statgov_data(BIN, LANG='ru') -> str:
    statgov_api_url = os.getenv('STATGOV_API_URL') \
                         .format(BIN=BIN, LANG=LANG)

    data = get_statgov_data_raw(BIN=BIN)

    result = ''

    for i, j in data.get('obj').items():
        result += f'<tr>' \
                  f'    <th>{i}</th>' \
                  f'    <th>{j}</th>' \
                  f'</tr>'

    return result


def get_goszakup_data(BIN: str) -> dict:
    URL = os.getenv('GOSZAKUP_URL')

    req = requests.get(
            URL.format(BIN=BIN),
            verify=False
    )

    soup = BeautifulSoup(req.text, 'html.parser')
    info = soup.select('table')

    return str(info)

# @retrier(max_retries=3, delay_seconds=3, exceptions=(Exception, ))
@retry(Exception)
def get_statgov_data_raw(BIN: str, LANG: str = 'ru'):
    statgov_api_url = os.getenv('STATGOV_API_URL') \
                        .format(BIN=BIN, LANG=LANG)

    data = requests.get(statgov_api_url)
    print(data)

    if data.status_code == 200:
        return data.json()
    else:
        raise Exception()

@retry(Exception)
def get_by_bin_data_egov(bin: str) -> dict:
    params = {
            "apiKey": os.getenv('DATA_EGOV_API_KEY'),
            "source": json.dumps({
                "query": {
                    "filtered": {
                        "filter": {
                            "bool": {
                                "must": [
                                    {
                                        "term": {
                                            "bin": bin,
                                        },
                                    },
                                ],
                            },
                        },
                    },
                },
            }),
        }
    response = httpx.get(url='https://data.egov.kz/api/v4/gbd_ul/v1', params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception()

def get_data_gov_string(BIN: str):
    data = get_by_bin_data_egov(BIN)

    result = ''
    for obj in data:
        for i, j in obj.items():
            result += f'<tr>' \
                    f'    <th>{i}</th>' \
                    f'    <th>{j}</th>' \
                    f'</tr>'

    return result

def agregate_data(BIN: str) -> str:
    print(BIN)
    with open('pdfexample.txt', 'r') as file:
        string_to_return = file.read() \
                               .format(STATGOV  = get_statgov_data(BIN=BIN),
                                       GOSZAKUP = get_goszakup_data(BIN=BIN),
                                       DATAEGOV = get_data_gov_string(BIN=BIN))

    return string_to_return
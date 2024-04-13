import time
import random


def drugs_service(iin: str):
    time.sleep(random.randint(5, 15))
    return True


def psycho_service(iin: str):
    time.sleep(random.randint(1, 5))
    return True


def crime_service(iin: str):
    time.sleep(random.randint(1, 15))
    return True
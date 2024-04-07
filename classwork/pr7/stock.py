
import time
import random


def stock1_service(articul: str):
    time.sleep(random.randint(5, 15))
    return (True, "Stock1")


def stock2_service(articul: str):
    time.sleep(random.randint(1, 5))
    return (False, "Stock2")


def stock3_service(articul: str):
    time.sleep(random.randint(1, 15))
    return (False, "Stock3")

def check(a):
    b = []
    for i in a:
        if i[0] == True:
            b.append(b[1])
    return b

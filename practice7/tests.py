import time 
import random


def test_checker(id: int):
    result = random.randint(10,15)
    time.sleep(result)
    return f"Passed, id = {id}  result = {result}" if result % 2 == 0 and id % 2 == 0 else f"Dont find your result, id = {id}"


    
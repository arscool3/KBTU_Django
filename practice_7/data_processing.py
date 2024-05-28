import time
import random

def process_data(data):
    time.sleep(random.randint(1, 5))
    return f"Processed data: {data}"

def analyze_data(data):
    time.sleep(random.randint(1, 5))
    return f"Analyzed data: {data}"

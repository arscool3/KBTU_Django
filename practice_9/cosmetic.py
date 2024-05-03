import time
import random

def anti_aging_service(id: str):
    time.sleep(random.randint(1, 5)) 
    return {"id": id, "name": "Anti-Aging Product", "description": "This is an anti-aging cosmetic product"}

def skin_care_service(id: str):
    time.sleep(random.randint(1, 5)) 
    return {"id": id, "name": "Skin Care Product", "description": "This is a skin care cosmetic product"}

def hair_care_service(id: str):
    time.sleep(random.randint(1, 5)) 
    return {"id": id, "name": "Hair Care Product", "description": "This is a hair care cosmetic product"}

import time
import random


def check_criminal_record(candidate_id: int) -> str:
    time.sleep(random.randint(5, 15))
    return f"Candidate {candidate_id} has a clean record."


def evaluate_skills(candidate_id: int) -> str:
    time.sleep(random.randint(3, 10))
    return f"Candidate {candidate_id} has relevant skills."


def conduct_interview(candidate_id: int) -> str:
    time.sleep(random.randint(7, 20))
    return f"Interview for candidate {candidate_id} completed successfully."

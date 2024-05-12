from datetime import timedelta

def calculate_amount(start_time, end_time):
    duration = end_time - start_time
    hours = duration.total_seconds() / 3600
    return hours * 100  # 100 тг за каждый час
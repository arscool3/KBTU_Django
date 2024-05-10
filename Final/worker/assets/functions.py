from datetime import datetime, timedelta

def get_expiration_timestamp(time):
    rounding_minutes = 5 - (time.minute % 5)

    if rounding_minutes != 0:
        time += timedelta(minutes=rounding_minutes)

    time += timedelta(minutes=5)

    return time

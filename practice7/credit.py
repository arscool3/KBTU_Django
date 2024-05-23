credit_history_data = {
    "123456789": True,
    "987654321": False,
    "567890123": True,
    "321098765": True,
    "456789012": False,
}
income_data = {
    "123456789": 12123,
    "987654321": 4132312,
    "567890123": 45451351252,
    "321098765": 5322351,
    "456789012": 535132325,
}

identity_data = {
    "123456789": True,
    "987654321": False,
    "567890123": True,
    "321098765": True,
    "456789012": False,
}


def check_credit_history(iin: str):
    return credit_history_data.get(iin, False)


def analyze_income(iin: str):
    return income_data.get(iin, 0)


def verify_identity(iin: str):
    return identity_data.get(iin, False)

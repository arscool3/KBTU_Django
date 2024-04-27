license_data = {
    "123456789": True,
    "987654321": False,
    "567890123": True,
    "321098765": True,
    "456789012": False,
}


category_data = {
    "123456789": 'A',
    "987654321": 'No license!',
    "567890123": 'B1',
    "321098765": 'C1',
    "456789012": 'No license!',
}


def check_license(iin: str):
    if iin in license_data.keys():
        return True
    else:
        return False


def verify_category(iin: str):
    if iin in category_data.keys():
        return category_data[iin]
    else:
        return False


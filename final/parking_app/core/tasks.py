import dramatiq

@dramatiq.actor
def print_invoice(user, invoice_data):
    print("Чек для пользователя:")
    print("Имя пользователя:", user.username)
    print("Данные чека:", invoice_data)

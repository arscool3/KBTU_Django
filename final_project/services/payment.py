from tasks import payment


async def create_payment():
    return payment.process_payment()

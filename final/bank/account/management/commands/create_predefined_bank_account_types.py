from django.core.management.base import BaseCommand
from account.models import BankAccountType

ACCOUNT_TYPES = [
    "Saving Account",
    "Checking Account",
    "Money Market Account",
    "Certificate of Deposit (CD)",
    "BankAccountType"
]

class Command(BaseCommand):
    help = 'Create predefined bank account types'

    def handle(self, *args, **kwargs):
        for account_type in ACCOUNT_TYPES:
            BankAccountType.objects.get_or_create(name=account_type)
        self.stdout.write(self.style.SUCCESS('Successfully created predefined bank account types'))

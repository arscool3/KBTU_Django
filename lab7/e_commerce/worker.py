# worker.py

import dramatiq

from django.core.management.base import BaseCommand
from dramatiq import Worker
from grocery.tasks import send_welcome_email

class Command(BaseCommand):
    help = 'Runs the Dramatiq worker'

    def handle(self, *args, **options):
        worker = Worker([send_welcome_email])
        worker.run()

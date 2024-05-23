import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MediConnectBackend.settings")
django.setup()

from django_dramatiq import get_broker

broker = get_broker()

from doctors.tasks import *

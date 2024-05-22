import os
import django
import sys
from dramatiq.cli import main as dramatiq_main 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_final.settings')
django.setup()

from shop.tasks import *
from shop.dramatiq import *

dramatiq_main("redis://localhost:6379", "shop.tasks") 


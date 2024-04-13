import os
import django
from dramatiq import Broker, set_broker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'practice7.settings')
django.setup()

broker = Broker(host='localhost', backend='redis://')
broker.connect()  

set_broker(broker)

from telegram import start_bot
from threading import Thread
from consumer import start_consumer

t1 = Thread(target=start_bot)
t2 = Thread(target=start_consumer)

# def startController():
t1.start()
t2.start()
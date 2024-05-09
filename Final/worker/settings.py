CELERY_BROKER_URL = "amqp://guest:guest@localhost:5672/"
CELERY_RESULT_BACKEND = "rpc://"

CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_ACCEPT_CONTENT = ["json"]

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = 'your_password'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_TIMEOUT = 10

SENDER_EMAIL = 'sender@example.com'
SENDER_NAME = 'Your Name'

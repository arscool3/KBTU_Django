from decouple import config

DATABASE_URL = config("DATABASE_URL")
SECRET_KEY = config("SECRET_KEY")
API_BASE_URL = config("API_BASE_URL")
API_KEY = config("API_KEY")

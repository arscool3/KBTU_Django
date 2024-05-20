from decouple import config

class Settings:
    PROJECT_NAME: str = "Video Streaming Platform"
    DB_USER: str = config("DB_USER")
    DB_PASS: str = config("DB_PASS")
    DB_HOST: str = config("DB_HOST")
    DB_PORT: int = int(config("DB_PORT"))  
    SECRET_KEY: str = config("SECRET_KEY")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

settings = Settings()

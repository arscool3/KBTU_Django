from decouple import config

class Settings:
    PROJECT_NAME: str = "Video Streaming Platform"
    DATABASE_URL: str = config("DATABASE_URL")
    SECRET_KEY: str = config("SECRET_KEY")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

settings = Settings()

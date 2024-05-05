from pydantic import BaseSettings

class Settings(BaseSettings):
    database_url: str = "postgresql://postgres:%211Qwerty1974%402@35.205.69.113:5432/diploma-db"


settings = Settings()

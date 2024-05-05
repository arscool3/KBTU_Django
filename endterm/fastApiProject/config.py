from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "airline_ticket_reservation"
    admin_email: str = "az_bazarbai@kbtu.kz"
    DATABASE_URL: str = "postgresql://postgres:password@localhost/airport"
    REDIS_URL: str = "redis://localhost:6379"
    SECRET_KEY: str = "3kaXiIR5IC520hkhBTAVxx59PIENu2zyvX4xV0M8XQciCwIS1TClGcpyXRGgjouDrh3DhviakR+qZhGYra9AHA=="
    REFRESH_SECRET_KEY: str = "u2zyvX4xV0M8XQciCwIS1TClhv3kaXiIR5IC520hkhBTAVxx59PIENiakR+qZhGYra9AHA=="
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 20
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60


settings = Settings()
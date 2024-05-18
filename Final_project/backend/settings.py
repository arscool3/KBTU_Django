from envparse import Env 

env = Env()

REAL_DATABASE_URL = env.str(
    "REAL_DATABASE_URL",
    default = "postgresql+asyncpg://postgres:admin@db:5432/egov"
)


SECRET_KEY: str = env.str("SECRET_KEY", default="secret_key")
ALGORITHM: str = env.str("ALGHORITHM", default="HS256")
ACCESS_TOKEN_EXPIRE_MINUTES: int = env.int("ACCESS_TOKEN_EXPIRE_MINUTES", default=30)

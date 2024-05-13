import asyncpg

PSQL_DETAILS = "postgres://postgres:12345@localhost:5432/postgres"


async def init_db():
    conn = await asyncpg.connect(PSQL_DETAILS)
    print("Connected to Database")
    return conn

from sqlalchemy import create_engine
from databases import Database

DATABASE_URL = "postgresql://username:password@localhost/my_fastapi_db"

engine = create_engine(DATABASE_URL)
database = Database(DATABASE_URL)
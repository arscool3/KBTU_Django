from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from databases import Database
from sqlalchemy.ext.declarative import declarative_base
from decouple import config

DATABASE_URL = config('DATABASE_URL')

engine = create_async_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()

database = Database(DATABASE_URL)

async def get_db():
    async with SessionLocal() as session:
        yield session

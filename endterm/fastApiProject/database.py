from asyncpg import types
from pydantic import BaseModel
from sqlalchemy import create_engine,String, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from passlib.context import CryptContext

from uuid import UUID
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:password@localhost/airport")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
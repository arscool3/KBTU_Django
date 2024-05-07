from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, Date, Boolean, Time, Table
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.orm import declarative_base
from passlib.context import CryptContext

Base = declarative_base()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(Base):
    __tablename__ = 'user'
    __table_args__ = {'schema': 'public'}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    iinbin = Column(String(12), unique=True, nullable=False, index=True)
    password = Column(String, nullable=False)
    fullname = Column(String(64), nullable=False)
    birthdate = Column(Date(), nullable=False)
    birthplace = Column(String(256), nullable=False)
    nation = Column(String(64), nullable=False)
    sex = Column(String(16), nullable=False)
    email = Column(String(64), nullable=True)
    phone_number = Column(String(12), nullable=True)
    address = Column(String(256), nullable=True)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password)

    def hash_password(self, password):
        return pwd_context.hash(password)

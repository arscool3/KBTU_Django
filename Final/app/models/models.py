from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, Date, Boolean, Time, Table, \
                       DateTime, func, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
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
    gender = Column(String(16), nullable=False)
    email = Column(String(64), nullable=True)
    phone_number = Column(String(12), nullable=True)
    address = Column(String(256), nullable=True)
    is_manager = Column(Boolean())
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, nullable=True)

    def __init__(self, iinbin, password, fullname, birthdate, birthplace, nation, gender, email=None, phone_number=None,
                 address=None, is_manager=False):
        self.iinbin = iinbin
        self.password = self.hash_password(password)
        self.fullname = fullname
        self.birthdate = birthdate
        self.birthplace = birthplace
        self.nation = nation
        self.gender = gender
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.is_manager = is_manager

    def verify_password(self, password):
        return pwd_context.verify(password, self.password)

    def hash_password(self, password):
        return pwd_context.hash(password)

class Application(Base):
    __tablename__ = 'application'
    __table_args__ = {'schema': 'public'}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey('public.user.id'), nullable=False)
    manager_id = Column(UUID(as_uuid=True), ForeignKey('public.user.id'), nullable=True)
    status = Column(String(12), nullable=False, default='Создано')
    created_at = Column(DateTime, nullable=False, default=func.now())
    updated_at = Column(DateTime, nullable=True)
    closed_at = Column(DateTime, nullable=True)

    user = relationship("User", foreign_keys=[user_id], backref="user_applications")
    manager = relationship("User", foreign_keys=[manager_id], backref="manager_applications")

    def __init__(self, user_id):
        self.user_id = user_id

class ProfileUpdateApplication(Base):
    __tablename__ = 'profile_update_application'
    __table_args__ = {'schema': 'public'}

    application_id = Column(UUID(as_uuid=True), ForeignKey('public.application.id'))
    key = Column(String(64), nullable=False)
    old_value = Column(String(256), nullable=True)
    new_value = Column(String(256), nullable=True)

    application = relationship("Application", backref="application_details")

    def __init__(self, application_id, key, old_value=None, new_value=None):
        self.application_id = application_id
        self.key = key
        self.old_value = old_value
        self.new_value = new_value

    __table_args__ = (
        PrimaryKeyConstraint('application_id', 'key'),
        {'schema': 'public'}
    )

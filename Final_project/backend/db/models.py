import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Boolean, String, Enum, Integer, ForeignKey, DateTime, JSON
from datetime import datetime
from typing import Optional

Base = declarative_base()

class PortalRole(str, Enum):
    ROLE_PORTAL_PHIS = "ROLE_PORTAL_PHIS"
    ROLE_PORTAL_MNG = "ROLE_PORTAL_MNG"

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable = False)
    surname = Column(String, nullable = False)
    email = Column(String, nullable = False, unique = True)   
    is_active = Column(Boolean(), default = True)    
    hashed_password = Column(String, nullable = False)
    roles = Column(String, nullable=False)
    tg_id = Column(String, nullable=False)
    iin = Column(String, nullable = False, unique = True) 
    birthdate = Column(String)
    age = Column(Integer)
    call = Column(String, nullable = False)
    city = Column(String)
    fact_address = Column(String)
    prop_address = Column(String)
    university = Column(String)
    

class Application(Base):
    __tablename__ = "applications"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(String, nullable=False)
    status = Column(String, default="Under consideration", nullable = False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)
    is_active = Column(Boolean(), default = True)    
    personal_data_changes = Column(JSON)

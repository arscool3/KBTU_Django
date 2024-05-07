from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

#db, user,password, db_name

url='postgresql://postgres:aru@localhost/fastapi2'

engine=create_engine(url)
session=Session(engine)

Base=declarative_base()
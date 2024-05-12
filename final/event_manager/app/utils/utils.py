
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt
from  models import models

# Get environment variables or secret key
SECRET_KEY = "e14bafafb7bac95d3bfdd463fe2b1e96c6e272cb0fcdf9c8"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Hashing utilities
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_pass(password:str):
   return pwd_context.hash(password)

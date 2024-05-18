from passlib.context import CryptContext
from typing import Annotated, Union
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from datetime import datetime, timedelta
from jose import jwt, JWTError
from database import get_db
from exceptions.auth_exceptions import credentials_exception, permission_exception
from schemas import auth_schemas as schemas

SECRET_KEY = "01d31b6eb6cd66725a02f8c496a61fab4a08ed731e88d01d1e6180e046ef876b"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="token",
    scopes={"student": "allow student actions", "instructor": "allow instructor actions"}
    )

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def authenticate_user(username: str, password: str, session: Annotated[str, Depends(get_db)]):
    from crud import auth_crud as crud
    user = crud.check_user_existense(username, session)
    if not user:
        return {"error": "user does not exist"}
    if not verify_password(password, user.password):
        return False
    return user


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        scopes: list = payload.get("scopes", [])
        if email is None:
            raise credentials_exception
        token_data = schemas.TokenData(email=email, scopes=scopes)
    except JWTError:
        raise credentials_exception
    return token_data

def require_scope(required_scope: str):
    def scope_dependency(scopes: Annotated[schemas.TokenData, Depends(get_current_user)]):
        if required_scope not in scopes.scopes:
            raise permission_exception
    return scope_dependency


def validate_user_by_email(email: str, token: Annotated[schemas.TokenData, Depends(require_scope)]):
    return email == token.email

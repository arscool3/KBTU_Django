from fastapi import Depends, HTTPException, Security
from fastapi.security import OAuth2PasswordBearer
from . import token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Security(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    user = token.verify_token(token)
    if user is None:
        raise credentials_exception
    return user
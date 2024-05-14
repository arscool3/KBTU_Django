from fastapi import APIRouter
from auth import schemas
from auth import crud
from typing import Annotated
from fastapi import Depends, HTTPException
from auth.utils import *
from database import get_db
from auth.exceptions import authentication_exception

router = APIRouter(
    prefix='/auth',
    tags=['authentication']
)


@router.post('/register')
def register(user: schemas.UserCreate, session: Annotated[str, Depends(get_db)]):
    crud.create_user(user, session)

    return {"message": "user successfully registered"}


@router.post('/login')
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], session: Annotated[str, Depends(get_db)]
) -> schemas.Token:
    user = authenticate_user(form_data.username, form_data.password, session)
    if not user:
        raise authentication_exception
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={
            "sub": user.username,
            "role": user.role.value
            }, 
            expires_delta=access_token_expires
    )
    return schemas.Token(access_token=access_token, token_type="bearer")
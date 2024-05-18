from fastapi import APIRouter
from typing import Annotated
from fastapi import Depends
from database import get_db
from utils.auth_forms import CustomOAuth2PasswordRequestForm
from utils.auth_utils import *
from exceptions.auth_exceptions import *
from models import auth_models as models
from crud import auth_crud as crud

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
    form_data: Annotated[CustomOAuth2PasswordRequestForm, Depends()], session: Annotated[str, Depends(get_db)]
):
    user = authenticate_user(form_data.username, form_data.password, session)
    if not user:
        raise authentication_exception
    
    scopes = []
    # return {"mess": user.role.value == models.RoleEnum.INSTRUCTOR.value}
    if(user.role.value == models.RoleEnum.INSTRUCTOR.value):
        scopes = ["instructor"]
    else:
        scopes = ["student"]
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={
            "sub": user.email,
            "scopes": scopes
            }, 
            expires_delta=access_token_expires
    )
    return schemas.Token(access_token=access_token, token_type="bearer")


@router.get("/user")
def get_token_user(user: Annotated[schemas.TokenData, Depends(get_current_user)]):
    return user


@router.get("/all")
def get_all_users(session: Annotated[str, Depends(get_db)]):
    return crud.get_all_users(session)
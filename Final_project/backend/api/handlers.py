from fastapi import APIRouter, Depends, HTTPException
from uuid import UUID

from typing import List

from sqlalchemy.ext.asyncio import AsyncSession
from api.models import UserCreate, ShowUser, ShowApplication, PersonalDataChange
from sqlalchemy.exc import IntegrityError

from logging import getLogger

from api.models import UpdatedUserResponse, UpdateUserRequest
from api.actions.user import _create_new_user, _get_user_by_id, _get_user_by_email
from api.actions.auth import get_current_user_from_token
from api.actions.application import _create_new_application, _update_user, _get_app_by_id, _get_all_applications, _no_update_user

from db.models import User
from db.session import get_db
from db.dals import UserDAL

logger = getLogger(__name__)
user_router = APIRouter()
manager_router = APIRouter()

@user_router.post("/register", response_model=ShowUser)
async def create_user(body: UserCreate, db: AsyncSession = Depends(get_db)) -> ShowUser:
    try:
        return await _create_new_user(body, db)
    except IntegrityError as err:
        logger.error(err)
        raise HTTPException(status_code=503, detail=f"Database error {err}")


@user_router.post("/", response_model=ShowApplication)
async def create_application(body: PersonalDataChange, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user_from_token)) -> ShowApplication:
    try:
        return await _create_new_application(body, db, current_user)    
    except IntegrityError as err:
        logger.error(err)
        raise HTTPException(status_code=503, detail=f"Database error {err}")
    
@manager_router.patch('/app', response_model=UpdatedUserResponse)
async def update_user_by_app(application_id: UUID, db: AsyncSession = Depends(get_db), 
                                   current_user: User = Depends(get_current_user_from_token)) -> UpdatedUserResponse:
    
    updated_applications_params = await _get_app_by_id(application_id, db)

    if current_user.roles == "ROLE_PORTAL_PHIS":
        raise HTTPException(status_code=403, detail=f"Doesn't have permissions")
    
    try:
        updated_user_id = await _update_user(updated_applications_params=updated_applications_params, session=db, id=application_id)
    except IntegrityError as err:
        logger.error(err)
        raise HTTPException(status_code=503, detail=f"Database error: {err}")     
    return UpdatedUserResponse(updated_user_id=updated_user_id)

@manager_router.get('/apps', response_model=List[ShowApplication])
async def get_applications(db: AsyncSession = Depends(get_db)) -> List[ShowApplication]:
    applications = await _get_all_applications(db)
    if not applications:
        raise HTTPException(status_code=404, detail="Applications not found")
    return applications

@user_router.patch('/', response_model=UpdatedUserResponse)
async def update_user_by_id(user_id: UUID, body: UpdateUserRequest, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user_from_token)) -> UpdatedUserResponse:
    updated_user_params = body.dict(exclude_none = True)
    if updated_user_params == {}:
        raise HTTPException(status_code=422, detail=f"At least one parameter for user update info should be provided")
    if user_id != current_user.user_id:
        raise HTTPException(status_code=403, detail=f"Forbidden")
    try:
        updated_user_id = await _update_user(updated_user_params=updated_user_params, session=db, user_id=user_id)
    except IntegrityError as err:
        logger.error(err)
        raise HTTPException(status_code=503, detail=f"Database error: {err}")     
    return UpdatedUserResponse(updated_user_id=updated_user_id)

# @user_router.patch('/', response_model=UpdatedUserResponse)
# async def no_update_user_by_id(user_id: UUID, body: UpdateUserRequest, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user_from_token)) -> UpdatedUserResponse:
#     updated_user_params = body.dict(exclude_none = True)
#     if updated_user_params == {}:
#         raise HTTPException(status_code=422, detail=f"At least one parameter for user update info should be provided")
#     if user_id != current_user.user_id:
#         raise HTTPException(status_code=403, detail=f"Forbidden")
#     try:
#         updated_user_id = await _update_user(updated_user_params=updated_user_params, session=db, user_id=user_id)
#     except IntegrityError as err:
#         logger.error(err)
#         raise HTTPException(status_code=503, detail=f"Database error: {err}")     
#     return UpdatedUserResponse(updated_user_id=updated_user_id)
@manager_router.patch('/no', response_model=UpdatedUserResponse)
async def no_update_user_by_app(application_id: UUID, db: AsyncSession = Depends(get_db), 
                                   current_user: User = Depends(get_current_user_from_token)) -> UpdatedUserResponse:

    if current_user.roles == "ROLE_PORTAL_PHIS":
        raise HTTPException(status_code=403, detail=f"Doesn't have permissions")
    
    try:
        updated_user_id = await _no_update_user(session=db, id=application_id)
    except IntegrityError as err:
        logger.error(err)
        raise HTTPException(status_code=503, detail=f"Database error: {err}")     
    return UpdatedUserResponse(updated_user_id=updated_user_id)

# @user_router.delete('/', response_model=DeleteUserResponse)
# async def delete_user(user_id: UUID, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user_from_token)) -> DeleteUserResponse:
#     user_for_deletion = await get_user_by_id(user_id, db)
#     if user_for_deletion is None:
#         raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")
#     if not check_user_permission(target_user=user_for_deletion, current_user=current_user):
#         raise HTTPException(status_code=403, detail="Forbidden")
#     deleted_user_id = await _delete_user(user_id, db)
#     return DeleteUserResponse(deleted_user_id=user_for_deletion)

# @user_router.get('/', response_model=ShowUser)
# async def get_user_by_id(id: UUID, db: AsyncSession = Depends(get_db)) -> ShowUser:
#     user = await _get_user_by_id(id, db)
#     if user is None:
#         raise HTTPException(status_code=404, detail=f"User with id {id} not found")
#     return user

@user_router.get('/{email}', response_model=ShowUser)
async def get_user_by_email(email: str, db: AsyncSession = Depends(get_db)) -> ShowUser:
    user = await _get_user_by_email(email, db)
    if user is None:
        raise HTTPException(status_code=404, detail=f"User with id {id} not found")
    return user


from uuid import UUID
from typing import List
from fastapi import Depends
from api.models import ShowApplication, PersonalDataChange, ShowUser
from api.actions.auth import get_current_user_from_token
from db.dals import UserDAL
from db.models import User, Application

async def _create_new_application(body: PersonalDataChange, session, current_user: User = Depends(get_current_user_from_token)) -> ShowApplication:
        async with session.begin():
            app_dal = UserDAL(session)

            if not body.name:
                body.name = current_user.name
            if not body.surname:
                body.surname = current_user.surname
            if not body.email:
                body.email = current_user.email
            if not body.tg_id:
                body.tg_id = current_user.tg_id
            if not body.iin:
                body.iin = current_user.iin
            if not body.birthdate:
                body.birthdate = current_user.birthdate
            if not body.age:
                body.age = current_user.age
            if not body.call:
                body.call = current_user.call
            if not body.city:
                body.city = current_user.city
            if not body.fact_address:
                body.fact_address = current_user.fact_address
            if not body.prop_address:
                body.prop_address = current_user.prop_address
            if not body.university:
                body.university = current_user.university

            app = await app_dal.submit_application(
                user_id=current_user.id,
                personal_data_changes=body.dict(),
            )
            return ShowApplication(
                id = app.id,
                user_id = app.user_id,
                status = app.status,
                created_at = app.created_at,
                updated_at = app.updated_at,
                is_active = app.is_active,
                personal_data_changes = app.personal_data_changes
            )

async def _update_user(updated_applications_params: dict, id: UUID, session) -> UUID:
        async with session.begin():
            app_dal = UserDAL(session)
            updated_user_id = await app_dal.update_user(
                id=id,
                **updated_applications_params
            )
            
            return updated_user_id

async def _no_update_user(id: UUID, session) -> UUID:
        async with session.begin():
            app_dal = UserDAL(session)
            updated_user_id = await app_dal.no_update_user(
                id=id,
            )
            return updated_user_id
        
async def _get_app_by_id(id, session) -> UUID:
        async with session.begin():
            user_dal = UserDAL(session)
            user = await user_dal.get_app_by_id(
                id = id,
            )
            return user

async def _get_all_applications(session) -> List[ShowApplication]:
    user_dal = UserDAL(session)
    applications = await user_dal.get_all_applications()
    return applications
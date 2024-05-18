from typing import Union
from uuid import UUID
from api.models import ShowUser, UserCreate
from db.dals import UserDAL
from hashing import Hasher
from db.dals import PortalRole

async def _create_new_user(body: UserCreate, session) -> ShowUser:
        async with session.begin():
            user_dal = UserDAL(session)
            user = await user_dal.create_user(
                name=body.name,
                surname=body.surname,
                email=body.email,
                hashed_password=Hasher.get_password_hash(body.password),
                iin = body.iin,
                call = body.call,
                tg_id = body.tg_id,
                roles = PortalRole.ROLE_PORTAL_PHIS
            )
            if user is not None:
                return user
        
# async def _delete_user(user_id, session) -> Union[UUID, None]:
#         async with session.begin():
#             user_dal = UserDAL(session)
#             deleted_user_id = await user_dal.delete_user(
#                 user_id = user_id,
#             )
#             return deleted_user_id

# async def _update_user(updated_user_params: dict, user_id: UUID, session) -> Union[UUID, None]:
#         async with session.begin():                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
#             user_dal = UserDAL(session)
#             updated_user_id = await user_dal.update_user(
#                 user_id=user_id,
#                 **updated_user_params
#             )
#             return updated_user_id

async def _get_user_by_id(id, session) -> Union[UUID, None]:
        async with session.begin():
            user_dal = UserDAL(session)
            user = await user_dal.get_user_by_id(
                id = id,
            )
            if user is not None:
                return user
            

async def _get_user_by_email(email, session) -> Union[UUID, None]:
        async with session.begin():
            user_dal = UserDAL(session)
            user = await user_dal.get_user_by_email(
                email = email,
            )
            if user is not None:
                return user


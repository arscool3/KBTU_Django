from db.models import User, PortalRole, Application
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Union
from uuid import UUID
from sqlalchemy import update, select, and_
from datetime import datetime
from fastapi import HTTPException



class UserDAL:
    def __init__(self, db_session:AsyncSession):
        self.db_session = db_session
    
    async def create_user(self, name:str, surname:str, email:str, hashed_password:str, roles: PortalRole, iin:str, call: str, tg_id: str) -> User:
        new_user = User(
                name=name,
                surname=surname,
                email=email,
                hashed_password=hashed_password,
                roles=roles,
                iin=iin,
                call=call,
                tg_id=tg_id
            )
        self.db_session.add(new_user)
        await self.db_session.flush()
        return new_user
    
    async def submit_application(self, user_id:str, personal_data_changes:dict) -> Application:
        query = select(Application.id).where(and_(Application.user_id == str(user_id)), (Application.status == "Under consideration"))
        res=await self.db_session.execute(query)
        user_row = res.fetchone()
        print(user_row)
        if user_row is not None:
            raise HTTPException(status_code=403, detail=f"Заявка не принимается")

        new_application = Application(
                user_id=str(user_id),
                personal_data_changes=personal_data_changes,
            )


        self.db_session.add(new_application)
        await self.db_session.flush()
        return new_application
    
    async def get_app_by_id(self, id: UUID) -> Union[UUID, None]:
        query = select(Application.personal_data_changes).where(Application.id == id)
        res=await self.db_session.execute(query)
        user_row = res.fetchone()
        return user_row.personal_data_changes
    
    async def update_user(self, id: UUID,  **kwargs) -> UUID:
        user_id_query = select(Application.user_id).where(Application.id == id)
        user_id_result = await self.db_session.execute(user_id_query)
        user_id_row = user_id_result.fetchone()
        user_id = user_id_row.user_id

        status = update(Application).where(Application.id == id).values(status="Processed")
        updated_at = update(Application).where(Application.id == id).values(updated_at=datetime.now())
        await self.db_session.execute(status)
        await self.db_session.execute(updated_at)


        # # Commit the changes
        # await self.db_session.commit()
        

        query = update(User).\
            where(User.id == UUID(user_id)).\
            values(**kwargs).\
            returning(User.id)

        res = await self.db_session.execute(query)
        updated_user = res.fetchone()
        print("Type of updated_user:1", type(updated_user[0]))
        print("Value of updated_user1:", updated_user[0])
        return updated_user[0]

    # async def delete_user(self, user_id: UUID) -> Union[UUID, None]:
    #     query = update(User).\
    #         where(and_(User.user_id == user_id, User.is_active == True)).\
    #         values(is_active=False).\
    #         returning(User.user_id)
    #     res=await self.db_session.execute(query)
    #     deleted_user_id_row = res.fetchone()
    #     if deleted_user_id_row is not None:
    #         return deleted_user_id_row[0]
    async def no_update_user(self, id: UUID) -> UUID:
        status = update(Application).where(Application.id == id).values(status="Rejected")
        await self.db_session.execute(status)
        id_user = select(Application.user_id).where(Application.id == id)
        updated_at = update(Application).where(Application.id == id).values(updated_at=datetime.now())
        await self.db_session.execute(updated_at)
        res = await self.db_session.execute(id_user)
        updated_user = res.fetchone()
        return UUID(updated_user[0])

    async def get_user_by_id(self, id: UUID) -> Union[UUID, None]:
        query = select(User).where(User.id == id)
        res=await self.db_session.execute(query)
        user_row = res.fetchone()
        if user_row is not None:
            return user_row[0]    
    
    
    async def get_user_by_email(self, email: str) -> Union[User, None]:
        query = select(User).where(User.email==email)
        res = await self.db_session.execute(query)
        user_row = res.fetchone()
        if user_row is not None:
            return user_row[0]
    
    async def get_all_applications(self):
        query = select(Application)
        result = await self.db_session.execute(query)
        applications = result.scalars().all()
        return applications
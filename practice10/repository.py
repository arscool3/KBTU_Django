# at least 1 dependency injection as class and 2 as methods


from abc import abstractmethod
from sqlalchemy.orm import Session
import models as db
from sqlalchemy import select
from schemas import Citizen,BaseModel,Country

class AbstractRepository:
    @abstractmethod
    def __init__(self,session:Session):
        pass

    @abstractmethod
    def get_by_id(self,id:int)->BaseModel:
        raise NotImplementedError()

class CitizenRepository(AbstractRepository):
    def __init__(self,session:Session):
        self._session=session
    # def get_all(self)->list[Citizen]:
    #     db_citizens=self._session.execute(select(db.Citizen)).scalars().all()
    #     citizens=[Citizen.model_validate(db_citizen) for db_citizen in db_citizens]
    #     return citizens
    def get_by_id(self,id:int)->Citizen:
        db_citizen=self._session.get(db.Citizen,id)
        return Citizen.model_validate(db_citizen)
    
class CountryRepository(AbstractRepository):
    def __init__(self,session:Session):
        self._session=session
    def get_by_id(self,id:int)->Country:
        pass
    
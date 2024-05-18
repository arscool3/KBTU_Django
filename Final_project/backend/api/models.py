import re
import uuid
from typing import Optional
from fastapi import HTTPException
from pydantic import BaseModel, EmailStr, validator, constr
from datetime import datetime

LETTER_MATCH_PATTERN = re.compile(r"^[a-яA-Яa-zA-Z\-]+$")

class TunedModel(BaseModel):
    class Config:
        orm_mode = True

class ShowUser(TunedModel):
    id: uuid.UUID
    name: str
    surname: str
    email: EmailStr
    is_active: bool
    roles: str
    tg_id: Optional[str] = None
    iin: Optional[str]= None
    birthdate: Optional[str]= None
    age: Optional[int]= None
    call: Optional[str]= None
    city: Optional[str]= None
    fact_address: Optional[str]= None
    prop_address: Optional[str]= None
    university: Optional[str]= None


class UserCreate(BaseModel):
    name: str
    surname: str
    email: EmailStr
    password: str
    iin: str
    call: str
    tg_id: str
    @validator("name")
    def validate_name(cls, value):
        if not LETTER_MATCH_PATTERN.match(value):
            raise HTTPException(status_code=422, default="Name should contains only letters")
        return value

    @validator("surname")
    def validate_surname(cls, value):
        if not LETTER_MATCH_PATTERN.match(value):
            raise HTTPException(status_code=422, default="Surname should contains only letters")
        return value

class ShowApplication(TunedModel):
    id: uuid.UUID
    user_id: str
    status: str
    created_at: datetime
    updated_at: datetime
    is_active: bool
    personal_data_changes: dict

class PersonalDataChange(BaseModel):
    name: Optional[str]
    surname: Optional[str]
    email: Optional[EmailStr]
    tg_id: Optional[str]
    iin: Optional[str]
    birthdate: Optional[str]
    age: Optional[int]
    call: Optional[str]
    city: Optional[str]
    fact_address: Optional[str]
    prop_address: Optional[str]
    university: Optional[str]
    def to_dict(self):
        return {
            "name": self.name,
            "surname": self.surname,
            "tg_id": self.tg_id,  
            "iin": self.iin,
            "birthdate": self.birthdate,
            "age": self.age,
            "call": self.call,
            "city": self.city,
            "fact_address": self.fact_address,
            "prop_address": self.prop_address,
            "university": self.university
        }
    # @validator("name")
    # def validate_name(cls, value):
    #     if not LETTER_MATCH_PATTERN.match(value):
    #         raise HTTPException(status_code=422, default="Name should contains only letters")
    #     return value

    # @validator("surname")
    # def validate_surname(cls, value):
    #     if not LETTER_MATCH_PATTERN.match(value):
    #         raise HTTPException(status_code=422, default="Surname should contains only letters")
    #     return value

class DeleteUserResponse(BaseModel):
    deleted_user_id: uuid.UUID

class UpdatedUserResponse(BaseModel):
    updated_user_id: uuid.UUID
 
class UpdateUserRequest(BaseModel):
    name: Optional[constr(min_length=1)]
    surname: Optional[constr(min_length=1)]    
    email: Optional[EmailStr]

    @validator("name")
    def validate_name(cls, value):
        if not LETTER_MATCH_PATTERN.match(value):
            raise HTTPException(status_code=422, default="Name should contains only letters")
        return value

    @validator("surname")
    def validate_surname(cls, value):
        if not LETTER_MATCH_PATTERN.match(value):
            raise HTTPException(status_code=422, default="Surname should contains only letters")
        return value

class Token(BaseModel):
    access_token: str
    token_type: str

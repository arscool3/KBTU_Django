from datetime import datetime

from pydantic import BaseModel

class User(BaseModel):
    first_name: str = ""
    last_name: str = ""
    middle_name: str = ""
    phone_number: str
    iin: str
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()


class UserLogin(BaseModel):
    phone_number: str
    iin: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "phone_number": "+77077525167",
                "iin": "000000000000",
            }
        }
    }

# schemas.py
from pydantic import BaseModel

class SeedBase(BaseModel):
    name: str
    description: str

class SeedCreate(SeedBase):
    pass

class SeedUpdate(SeedBase):
    pass

class Seed(SeedBase):
    id: int

    class Config:
        orm_mode = True

# Define other schemas here if needed

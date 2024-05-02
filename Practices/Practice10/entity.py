import pydantic


class Product(pydantic.BaseModel):
    id: int = pydantic.Field(ge=0)
    name: str = pydantic.Field(max_length=255)
    cost: int = pydantic.Field(ge=0)
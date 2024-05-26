from fastapi import APIRouter, Depends
from ..dependencies.config import get_config, Config

router = APIRouter()

@router.get("/config/")
async def get_configuration(config: Config = Depends(get_config)):
    return {"secret_key": config.secret_key}

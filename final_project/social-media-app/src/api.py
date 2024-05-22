## all routes
from fastapi import APIRouter

from .auth.views import router as auth_router

router = APIRouter(prefix="/v1")

router.include_router(router)

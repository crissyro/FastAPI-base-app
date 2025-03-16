from fastapi import APIRouter

from core.config import settings


router = APIRouter(
    prefix=settings.api_prefix.v1.users, 
    tags=["Users"],
)


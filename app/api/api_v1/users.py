from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from crud import crud_users
from core.schemas.user_schemas import UserCreate, UserRead
from core.config import settings


router = APIRouter(
    prefix=settings.api_prefix.v1.users, 
    tags=["Users"],
)

@router.get("", response_model=list[UserRead])
async def get_users(
    session: Annotated[
        AsyncSession, 
        Depends(db_helper.session_getter)
        ],
    ):
    users = await crud_users.get_all_users(session=session)
    return users

@router.post("", response_model=UserRead)
async def create_user(
    user_create: UserCreate,
    session: Annotated[
        AsyncSession, 
        Depends(db_helper.session_getter)
        ],
    ):
    user = await crud_users.create_user(
        session,
        user_create, 
    )
    return user
    
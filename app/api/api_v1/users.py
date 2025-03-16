from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from crud.crud_users import get_all_users
from core.schemas.user_schemas import UserRead
from core.config import settings


router = APIRouter(
    prefix=settings.api_prefix.v1.users, 
    tags=["Users"],
)

@router.get("")
async def get_users(
    session: AsyncSession = Depends(db_helper.session_getter),
    ):
    users = await get_all_users(session=session)
    return users
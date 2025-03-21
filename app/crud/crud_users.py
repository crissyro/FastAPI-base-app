from typing import Sequence
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.schemas.user_schemas import UserCreate
from core.models.user import User


async def get_all_users(session: AsyncSession) -> Sequence[User]:
    statement = select(User).order_by(User.id)
    result = await session.scalars(statement=statement)
    return result.all()


async def create_user(session: AsyncSession, user_create: UserCreate) -> User:
    new_user = User(**user_create.model_dump())
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return new_user

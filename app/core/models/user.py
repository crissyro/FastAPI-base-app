from datetime import datetime

from sqlalchemy import CheckConstraint, Index, UniqueConstraint
from .base import Base
from sqlalchemy.orm import Mapped, mapped_column

class User(Base):
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    is_active: Mapped[bool] = mapped_column(default=True)
    is_superuser: Mapped[bool] = mapped_column(default=False)
    last_login_at: Mapped[datetime] = mapped_column(nullable=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now())
    
    __table_args__ = (
        Index('idx_users_username', 'username'),
        Index('idx_users_email', 'email'),
        Index('idx_users_is_active', 'is_active'),
        Index('idx_users_is_superuser', 'is_superuser'),
        Index('idx_users_last_login_at', 'last_login_at'),
        Index('idx_users_created_at', 'created_at'),
        CheckConstraint('is_active IN (0, 1)', name='ck_users_is_active'),
        CheckConstraint('is_superuser IN (0, 1)', name='ck_users_is_superuser'),
        UniqueConstraint('username', 'email', name='uq_users_username_email'),
    )
    
"""del cols

Revision ID: 2516ea605baf
Revises: 45dc3840c591
Create Date: 2025-03-16 23:26:34.107398

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "2516ea605baf"
down_revision: Union[str, None] = "45dc3840c591"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.drop_index("idx_users_created_at", table_name="users")
    op.drop_index("idx_users_last_login_at", table_name="users")
    op.drop_column("users", "last_login_at")
    op.drop_column("users", "created_at")


def downgrade() -> None:
    """Downgrade schema."""
    op.add_column(
        "users",
        sa.Column(
            "created_at",
            postgresql.TIMESTAMP(),
            autoincrement=False,
            nullable=False,
        ),
    )
    op.add_column(
        "users",
        sa.Column(
            "last_login_at",
            postgresql.TIMESTAMP(),
            autoincrement=False,
            nullable=True,
        ),
    )
    op.create_index(
        "idx_users_last_login_at", "users", ["last_login_at"], unique=False
    )
    op.create_index(
        "idx_users_created_at", "users", ["created_at"], unique=False
    )

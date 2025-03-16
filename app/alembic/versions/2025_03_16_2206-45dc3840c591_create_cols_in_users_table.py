"""create cols in users table

Revision ID: 45dc3840c591
Revises: 0c2735e78bb7
Create Date: 2025-03-16 22:06:31.725317

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "45dc3840c591"
down_revision: Union[str, None] = "0c2735e78bb7"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("users", sa.Column("email", sa.String(), nullable=False))
    op.add_column("users", sa.Column("is_active", sa.Boolean(), nullable=False))
    op.add_column(
        "users", sa.Column("is_superuser", sa.Boolean(), nullable=False)
    )
    op.add_column(
        "users", sa.Column("last_login_at", sa.DateTime(), nullable=True)
    )
    op.add_column(
        "users", sa.Column("created_at", sa.DateTime(), nullable=False)
    )
    op.create_index(
        "idx_users_created_at", "users", ["created_at"], unique=False
    )
    op.create_index("idx_users_email", "users", ["email"], unique=False)
    op.create_index("idx_users_is_active", "users", ["is_active"], unique=False)
    op.create_index(
        "idx_users_is_superuser", "users", ["is_superuser"], unique=False
    )
    op.create_index(
        "idx_users_last_login_at", "users", ["last_login_at"], unique=False
    )
    op.create_index("idx_users_username", "users", ["username"], unique=False)
    op.create_unique_constraint(op.f("uq_users_email"), "users", ["email"])
    op.create_unique_constraint(
        "uq_users_username_email", "users", ["username", "email"]
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint("uq_users_username_email", "users", type_="unique")
    op.drop_constraint(op.f("uq_users_email"), "users", type_="unique")
    op.drop_index("idx_users_username", table_name="users")
    op.drop_index("idx_users_last_login_at", table_name="users")
    op.drop_index("idx_users_is_superuser", table_name="users")
    op.drop_index("idx_users_is_active", table_name="users")
    op.drop_index("idx_users_email", table_name="users")
    op.drop_index("idx_users_created_at", table_name="users")
    op.drop_column("users", "created_at")
    op.drop_column("users", "last_login_at")
    op.drop_column("users", "is_superuser")
    op.drop_column("users", "is_active")
    op.drop_column("users", "email")

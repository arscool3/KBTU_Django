"""initial commit

Revision ID: 79760a99c9f6
Revises: 
Create Date: 2024-05-20 19:33:21.949898

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '79760a99c9f6'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create the users table
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("username", sa.String, unique=True, index=True),
        sa.Column("email", sa.String, unique=True, index=True),
        sa.Column("hashed_password", sa.String),
        sa.Column("is_active", sa.Boolean, default=True),
    )


def downgrade() -> None:
    op.drop_table("users")

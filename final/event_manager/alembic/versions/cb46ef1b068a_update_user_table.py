"""update_user_table

Revision ID: cb46ef1b068a
Revises: f20cedc57db3
Create Date: 2024-05-11 18:13:28.066155

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cb46ef1b068a'
down_revision: Union[str, None] = 'f20cedc57db3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

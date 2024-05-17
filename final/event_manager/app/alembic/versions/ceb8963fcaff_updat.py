"""updat

Revision ID: ceb8963fcaff
Revises: 3deea29304e0
Create Date: 2024-05-16 20:16:44.922567

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ceb8963fcaff'
down_revision: Union[str, None] = '3deea29304e0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

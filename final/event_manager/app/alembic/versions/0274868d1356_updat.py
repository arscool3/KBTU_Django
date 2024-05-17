"""updat

Revision ID: 0274868d1356
Revises: ceb8963fcaff
Create Date: 2024-05-16 20:16:48.123611

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0274868d1356'
down_revision: Union[str, None] = 'ceb8963fcaff'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

"""another one

Revision ID: 0341e597998f
Revises: 9272bfe463b8
Create Date: 2024-05-21 20:21:43.341993

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0341e597998f'
down_revision: Union[str, None] = '9272bfe463b8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

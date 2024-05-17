"""updat

Revision ID: 93b3b9f48cf4
Revises: 0274868d1356
Create Date: 2024-05-16 20:16:55.324289

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '93b3b9f48cf4'
down_revision: Union[str, None] = '0274868d1356'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

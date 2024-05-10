"""New is_confirmed, expires_at  column in Application table

Revision ID: 68dcdffe660e
Revises: c62366cb0b02
Create Date: 2024-05-10 18:59:37.265790

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '68dcdffe660e'
down_revision: Union[str, None] = 'c62366cb0b02'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('application', sa.Column('is_confirmed', sa.Boolean(), nullable=True))
    op.add_column('application', sa.Column('expires_at', sa.DateTime(), nullable=True))
    op.drop_constraint('application_user_id_fkey', 'application', type_='foreignkey')
    op.drop_constraint('application_manager_id_fkey', 'application', type_='foreignkey')
    op.create_foreign_key(None, 'application', 'user', ['user_id'], ['id'], source_schema='public', referent_schema='public')
    op.create_foreign_key(None, 'application', 'user', ['manager_id'], ['id'], source_schema='public', referent_schema='public')
    op.drop_constraint('profile_update_application_application_id_fkey', 'profile_update_application', type_='foreignkey')
    op.create_foreign_key(None, 'profile_update_application', 'application', ['application_id'], ['id'], source_schema='public', referent_schema='public')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'profile_update_application', schema='public', type_='foreignkey')
    op.create_foreign_key('profile_update_application_application_id_fkey', 'profile_update_application', 'application', ['application_id'], ['id'])
    op.drop_constraint(None, 'application', schema='public', type_='foreignkey')
    op.drop_constraint(None, 'application', schema='public', type_='foreignkey')
    op.create_foreign_key('application_manager_id_fkey', 'application', 'user', ['manager_id'], ['id'])
    op.create_foreign_key('application_user_id_fkey', 'application', 'user', ['user_id'], ['id'])
    op.drop_column('application', 'expires_at')
    op.drop_column('application', 'is_confirmed')
    # ### end Alembic commands ###

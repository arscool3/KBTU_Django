"""Update expires_at  column in Application table 

Revision ID: bfe252480354
Revises: 68dcdffe660e
Create Date: 2024-05-10 20:08:30.931718

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bfe252480354'
down_revision: Union[str, None] = '68dcdffe660e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('application_user_id_fkey', 'application', type_='foreignkey')
    op.drop_constraint('application_manager_id_fkey', 'application', type_='foreignkey')
    op.create_foreign_key(None, 'application', 'user', ['manager_id'], ['id'], source_schema='public', referent_schema='public')
    op.create_foreign_key(None, 'application', 'user', ['user_id'], ['id'], source_schema='public', referent_schema='public')
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
    # ### end Alembic commands ###

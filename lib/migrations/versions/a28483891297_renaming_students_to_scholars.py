"""Renaming students to scholars

Revision ID: a28483891297
Revises: 791279dd0760
Create Date: 2023-08-31 17:36:45.888258

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a28483891297'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')

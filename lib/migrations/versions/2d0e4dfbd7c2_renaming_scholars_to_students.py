"""Renaming scholars to students

Revision ID: 2d0e4dfbd7c2
Revises: a28483891297
Create Date: 2023-08-31 17:56:20.169934

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d0e4dfbd7c2'
down_revision = 'a28483891297'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('scholars', 'students')


def downgrade() -> None:
    op.rename_table('students', 'scholars')
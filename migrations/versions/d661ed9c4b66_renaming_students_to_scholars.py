"""Renaming students to scholars

Revision ID: d661ed9c4b66
Revises: 10a59eb36117
Create Date: 2025-06-01 19:27:13.259046

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd661ed9c4b66'
down_revision: Union[str, None] = '10a59eb36117'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.alter_column('scholars', 'name', new_column_name='full_name')

def downgrade():
    op.alter_column('scholars', 'full_name', new_column_name='name')

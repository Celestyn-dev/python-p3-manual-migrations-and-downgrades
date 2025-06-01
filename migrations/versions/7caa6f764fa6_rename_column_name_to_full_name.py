"""Rename column name to full_name

Revision ID: 7caa6f764fa6
Revises: d661ed9c4b66
Create Date: 2025-06-01 19:33:57.730994

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7caa6f764fa6'
down_revision: Union[str, None] = 'd661ed9c4b66'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

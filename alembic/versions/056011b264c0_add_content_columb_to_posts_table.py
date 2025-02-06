"""add content columb to posts table

Revision ID: 056011b264c0
Revises: db65a846134f
Create Date: 2025-02-05 14:48:14.922303

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '056011b264c0'
down_revision: Union[str, None] = 'db65a846134f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content',sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass

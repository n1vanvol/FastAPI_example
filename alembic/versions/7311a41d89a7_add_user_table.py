"""add user table

Revision ID: 7311a41d89a7
Revises: 056011b264c0
Create Date: 2025-02-05 15:16:58.695255

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7311a41d89a7'
down_revision: Union[str, None] = '056011b264c0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    print("🚀 Running upgrade migration!")  # Добавляем вывод в консоль
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column("created_at", sa.TIMESTAMP(timezone=True),
                            server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'))



def downgrade() -> None:
    #op.drop_table('users')
    pass

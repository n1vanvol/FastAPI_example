"""create posts table

Revision ID: db65a846134f
Revises: 
Create Date: 2025-02-05 14:37:56.117396

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'db65a846134f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Создаем таблицу posts с двумя колонками: id и title
    op.create_table(
        'posts',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('title', sa.String(), nullable=False)
    )

def downgrade() -> None:
    # Удаляем таблицу posts при откате миграции
    op.drop_table('posts')

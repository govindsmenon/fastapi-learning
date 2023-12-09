"""add content column to posts table

Revision ID: 17d0495f4aac
Revises: 67d722b6c907
Create Date: 2023-12-08 23:46:08.722133

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '17d0495f4aac'
down_revision: Union[str, None] = '67d722b6c907'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column('posts', 'content')

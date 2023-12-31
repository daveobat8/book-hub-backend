"""Create Books table

Revision ID: d436aef751c7
Revises: 
Create Date: 2023-12-14 23:07:45.495642

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd436aef751c7'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.Text(), nullable=False),
    sa.Column('description', sa.VARCHAR(), nullable=False),
    sa.Column('author', sa.Text(), nullable=False),
    sa.Column('image', sa.VARCHAR(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('added_at', sa.TIMESTAMP(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('books')
    # ### end Alembic commands ###

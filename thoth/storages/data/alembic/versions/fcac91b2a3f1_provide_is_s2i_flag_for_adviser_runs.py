"""Provide is_s2i flag for adviser runs

Revision ID: fcac91b2a3f1
Revises: 9b210f8d5c24
Create Date: 2019-12-07 13:39:32.620452+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fcac91b2a3f1'
down_revision = '9b210f8d5c24'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('adviser_run', sa.Column('is_s2i', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('adviser_run', 'is_s2i')
    # ### end Alembic commands ###

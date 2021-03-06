"""add_confirmation_column

Revision ID: 2e00d812e406
Revises: 09c96fd0e48f
Create Date: 2017-09-29 22:54:14.649996

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e00d812e406'
down_revision = '09c96fd0e48f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('risk_factors', sa.Column('confirmation', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('risk_factors', 'confirmation')
    # ### end Alembic commands ###

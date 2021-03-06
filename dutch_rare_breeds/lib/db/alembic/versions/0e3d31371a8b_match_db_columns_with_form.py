"""match db columns with form

Revision ID: 0e3d31371a8b
Revises: 3b97fe3333c5
Create Date: 2017-10-11 21:35:34.217837

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e3d31371a8b'
down_revision = '3b97fe3333c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('risk_factors', sa.Column('N_active_breeders', sa.Integer(), nullable=True))
    op.add_column('risk_factors', sa.Column('N_breed_keeping_members', sa.Integer(), nullable=True))
    op.add_column('risk_factors', sa.Column('N_breeding_females', sa.Integer(), nullable=True))
    op.add_column('risk_factors', sa.Column('N_breeding_males', sa.Integer(), nullable=True))
    op.add_column('risk_factors', sa.Column('abroad_examples', sa.String(length=200), nullable=True))
    op.add_column('risk_factors', sa.Column('activities', sa.String(length=50), nullable=True))
    op.add_column('risk_factors', sa.Column('breed_present_abroad', sa.Integer(), nullable=True))
    op.add_column('risk_factors', sa.Column('breeding_limitations', sa.String(length=50), nullable=True))
    op.add_column('risk_factors', sa.Column('continuity_breeding', sa.Integer(), nullable=True))
    op.add_column('risk_factors', sa.Column('cryobank', sa.Integer(), nullable=True))
    op.add_column('risk_factors', sa.Column('elements_breeding_program', sa.String(length=50), nullable=True))
    op.add_column('risk_factors', sa.Column('governmental_support', sa.String(length=50), nullable=True))
    op.add_column('risk_factors', sa.Column('herdbook', sa.Integer(), nullable=True))
    op.add_column('risk_factors', sa.Column('name_association', sa.String(length=100), nullable=True))
    op.add_column('risk_factors', sa.Column('output_examples', sa.String(length=200), nullable=True))
    op.add_column('risk_factors', sa.Column('professional_members', sa.Integer(), nullable=True))
    op.add_column('risk_factors', sa.Column('profitable_output', sa.Integer(), nullable=True))
    op.add_column('risk_factors', sa.Column('promotion', sa.String(length=50), nullable=True))
    op.add_column('risk_factors', sa.Column('provinces', sa.String(length=50), nullable=True))
    op.add_column('risk_factors', sa.Column('specialty_examples', sa.String(length=200), nullable=True))
    op.add_column('risk_factors', sa.Column('specialty_use', sa.Integer(), nullable=True))
    op.add_column('risk_factors', sa.Column('support_examples', sa.String(length=200), nullable=True))
    op.drop_column('risk_factors', 'factor_three')
    op.drop_column('risk_factors', 'factor_two')
    op.drop_column('risk_factors', 'factor_five')
    op.drop_column('risk_factors', 'factor_four')
    op.drop_column('risk_factors', 'factor_one')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('risk_factors', sa.Column('factor_one', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('risk_factors', sa.Column('factor_four', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('risk_factors', sa.Column('factor_five', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('risk_factors', sa.Column('factor_two', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('risk_factors', sa.Column('factor_three', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('risk_factors', 'support_examples')
    op.drop_column('risk_factors', 'specialty_use')
    op.drop_column('risk_factors', 'specialty_examples')
    op.drop_column('risk_factors', 'provinces')
    op.drop_column('risk_factors', 'promotion')
    op.drop_column('risk_factors', 'profitable_output')
    op.drop_column('risk_factors', 'professional_members')
    op.drop_column('risk_factors', 'output_examples')
    op.drop_column('risk_factors', 'name_association')
    op.drop_column('risk_factors', 'herdbook')
    op.drop_column('risk_factors', 'governmental_support')
    op.drop_column('risk_factors', 'elements_breeding_program')
    op.drop_column('risk_factors', 'cryobank')
    op.drop_column('risk_factors', 'continuity_breeding')
    op.drop_column('risk_factors', 'breeding_limitations')
    op.drop_column('risk_factors', 'breed_present_abroad')
    op.drop_column('risk_factors', 'activities')
    op.drop_column('risk_factors', 'abroad_examples')
    op.drop_column('risk_factors', 'N_breeding_males')
    op.drop_column('risk_factors', 'N_breeding_females')
    op.drop_column('risk_factors', 'N_breed_keeping_members')
    op.drop_column('risk_factors', 'N_active_breeders')
    # ### end Alembic commands ###

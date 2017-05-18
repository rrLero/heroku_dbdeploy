"""add tables

Revision ID: 691e545b4285
Revises: 
Create Date: 2017-05-18 14:24:07.052772

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '691e545b4285'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('player',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('player_name', sa.String(), nullable=True),
    sa.Column('player_surname', sa.String(), nullable=True),
    sa.Column('photo_path', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tournaments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('player_id', sa.Integer(), nullable=False),
    sa.Column('place', sa.Integer(), nullable=False),
    sa.Column('points', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['player_id'], ['player.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tournaments')
    op.drop_table('player')
    # ### end Alembic commands ###
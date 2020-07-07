"""'blacklist'

Revision ID: 51822fe1a801
Revises: 280db886c8f9
Create Date: 2020-07-07 15:37:08.170851

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51822fe1a801'
down_revision = '280db886c8f9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blacklist_tokens',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('token', sa.String(length=500), nullable=False),
    sa.Column('blacklisted_on', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blacklist_tokens')
    # ### end Alembic commands ###

"""empty message

Revision ID: b261744318c1
Revises: eb172ac2708b
Create Date: 2018-09-13 09:39:16.848331

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b261744318c1'
down_revision = 'eb172ac2708b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tbl_vsppm_company',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('admin', sa.String(length=60), nullable=True),
    sa.Column('website', sa.String(length=128), nullable=True),
    sa.Column('created_ts', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_ts', sa.DateTime(timezone=True), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tbl_vsppm_company')
    # ### end Alembic commands ###

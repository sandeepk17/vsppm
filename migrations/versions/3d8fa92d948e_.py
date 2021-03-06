"""empty message

Revision ID: 3d8fa92d948e
Revises: 0d9090e0d37e
Create Date: 2018-09-17 10:29:03.014129

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d8fa92d948e'
down_revision = '0d9090e0d37e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tbl_vsppm_project',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=90), nullable=False),
    sa.Column('begin', sa.DateTime(timezone=True), nullable=True),
    sa.Column('end', sa.DateTime(timezone=True), nullable=True),
    sa.Column('type', sa.String(length=20), nullable=True),
    sa.Column('days', sa.Integer(), nullable=True),
    sa.Column('status', sa.String(length=30), nullable=True),
    sa.Column('desc', sa.String(length=256), nullable=True),
    sa.Column('opened_by_id', sa.Integer(), nullable=True),
    sa.Column('opened_datetime', sa.DateTime(timezone=True), nullable=True),
    sa.Column('closed_by_id', sa.Integer(), nullable=True),
    sa.Column('closed_datetime', sa.DateTime(timezone=True), nullable=True),
    sa.Column('canceled_by_id', sa.Integer(), nullable=True),
    sa.Column('canceled_datetime', sa.DateTime(timezone=True), nullable=True),
    sa.Column('manager_admin_id', sa.Integer(), nullable=True),
    sa.Column('test_admin_id', sa.Integer(), nullable=True),
    sa.Column('release_admin_id', sa.Integer(), nullable=True),
    sa.Column('require_admin_id', sa.Integer(), nullable=True),
    sa.Column('access', sa.String(length=20), nullable=True),
    sa.Column('created_ts', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_ts', sa.DateTime(timezone=True), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['canceled_by_id'], ['tbl_vsppm_user.id'], ),
    sa.ForeignKeyConstraint(['closed_by_id'], ['tbl_vsppm_user.id'], ),
    sa.ForeignKeyConstraint(['manager_admin_id'], ['tbl_vsppm_user.id'], ),
    sa.ForeignKeyConstraint(['opened_by_id'], ['tbl_vsppm_user.id'], ),
    sa.ForeignKeyConstraint(['release_admin_id'], ['tbl_vsppm_user.id'], ),
    sa.ForeignKeyConstraint(['require_admin_id'], ['tbl_vsppm_user.id'], ),
    sa.ForeignKeyConstraint(['test_admin_id'], ['tbl_vsppm_user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('tbl_vsppm_project_member',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('project_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['project_id'], ['tbl_vsppm_project.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['tbl_vsppm_user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'project_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tbl_vsppm_project_member')
    op.drop_table('tbl_vsppm_project')
    # ### end Alembic commands ###

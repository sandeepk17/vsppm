"""empty message

Revision ID: 0d9090e0d37e
Revises: f730fd3b0af3
Create Date: 2018-09-16 20:59:13.300370

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0d9090e0d37e'
down_revision = 'f730fd3b0af3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tbl_vsppm_user_role')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tbl_vsppm_user_role',
    sa.Column('user_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('role_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['role_id'], ['tbl_vsppm_role.id'], name='tbl_vsppm_user_role_ibfk_1'),
    sa.ForeignKeyConstraint(['user_id'], ['tbl_vsppm_user.id'], name='tbl_vsppm_user_role_ibfk_2'),
    sa.PrimaryKeyConstraint('user_id', 'role_id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###

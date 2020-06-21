"""empty message

Revision ID: 1bdd017b9560
Revises: 4b58c9b3d57e
Create Date: 2020-04-22 09:10:08.819000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1bdd017b9560'
down_revision = '4b58c9b3d57e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###

    op.add_column('members', sa.Column('subscribe', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('members', 'subscribe')
    op.create_table('course',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'latin1',
    mysql_engine=u'InnoDB'
    )
    op.create_table('test',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'latin1',
    mysql_engine=u'InnoDB'
    )
    op.create_table('order',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('price', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('member_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['member_id'], [u'member.id'], name=u'order_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'latin1',
    mysql_engine=u'InnoDB'
    )
    op.create_table('user_courses',
    sa.Column('member_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('course_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['course_id'], [u'course.id'], name=u'user_courses_ibfk_2'),
    sa.ForeignKeyConstraint(['member_id'], [u'member.id'], name=u'user_courses_ibfk_1'),
    mysql_default_charset=u'latin1',
    mysql_engine=u'InnoDB'
    )
    op.create_table('member',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('username', mysql.VARCHAR(length=30), nullable=True),
    sa.Column('password', mysql.VARCHAR(length=30), nullable=True),
    sa.Column('email', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('join_date', mysql.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'latin1',
    mysql_engine=u'InnoDB'
    )
    op.create_index('username', 'member', ['username'], unique=True)
    # ### end Alembic commands ###

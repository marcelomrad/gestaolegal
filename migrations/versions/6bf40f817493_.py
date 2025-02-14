"""empty message

Revision ID: 6bf40f817493
Revises: e184e0eb7d30
Create Date: 2021-10-20 12:12:11.674979

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6bf40f817493'
down_revision = 'e184e0eb7d30'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###

    op.alter_column('enderecos', 'cep',
               existing_type=mysql.VARCHAR(charset='latin1', collation='latin1_general_ci', length=9),
               type_=sa.String(length=10, collation='latin1_general_ci'),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('enderecos', 'cep',
               existing_type=sa.String(length=10, collation='latin1_general_ci'),
               type_=mysql.VARCHAR(charset='latin1', collation='latin1_general_ci', length=9),
               existing_nullable=False)
    # ### end Alembic commands ###

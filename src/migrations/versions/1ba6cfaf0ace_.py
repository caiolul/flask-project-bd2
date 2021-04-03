"""empty message

Revision ID: 1ba6cfaf0ace
Revises: 6ee00e656ed9
Create Date: 2021-03-31 20:27:33.327894

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1ba6cfaf0ace'
down_revision = '6ee00e656ed9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('state',
    sa.Column('cnpj', sa.String(length=120), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('cnpj'),
    sa.UniqueConstraint('cnpj')
    )
    op.create_table('country',
    sa.Column('cnpj', sa.String(length=120), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('state_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['state_id'], ['state.cnpj'], ),
    sa.PrimaryKeyConstraint('cnpj'),
    sa.UniqueConstraint('cnpj')
    )
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=80), nullable=False),
    sa.Column('email', sa.VARCHAR(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('country')
    op.drop_table('state')
    # ### end Alembic commands ###
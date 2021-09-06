"""empty message

Revision ID: 30e8ff61ff06
Revises: f8b4e1397bbd
Create Date: 2021-08-09 15:03:10.032140

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30e8ff61ff06'
down_revision = 'f8b4e1397bbd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), server_default='1', nullable=True))
        batch_op.create_foreign_key(None, 'user', ['user_id'], ['id'], ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
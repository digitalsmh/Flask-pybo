"""empty message

Revision ID: 5b44fe7e305d
Revises: 93fc02781722
Create Date: 2023-09-10 21:48:38.461499

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b44fe7e305d'
down_revision = '93fc02781722'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###

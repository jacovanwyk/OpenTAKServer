"""Added publish_time to packages table

Revision ID: 34d5df698b81
Revises: 34dc96ee805b
Create Date: 2024-09-12 17:47:08.855213

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34d5df698b81'
down_revision = '34dc96ee805b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('device_profiles', schema=None) as batch_op:
        batch_op.alter_column('preference_key',
               existing_type=sa.String(length=255),
               nullable=False)

    with op.batch_alter_table('packages', schema=None) as batch_op:
        batch_op.add_column(sa.Column('publish_time', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('packages', schema=None) as batch_op:
        batch_op.drop_column('publish_time')

    with op.batch_alter_table('device_profiles', schema=None) as batch_op:
        batch_op.alter_column('preference_key',
               existing_type=sa.String(length=255),
               nullable=True)

    # ### end Alembic commands ###

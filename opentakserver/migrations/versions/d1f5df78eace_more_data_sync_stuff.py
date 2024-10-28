"""More data sync stuff

Revision ID: d1f5df78eace
Revises: 4f0173cdb93b
Create Date: 2024-10-15 03:02:43.059600

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1f5df78eace'
down_revision = '4f0173cdb93b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('mission_changes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('content_uid', sa.String(length=255), nullable=True))
        batch_op.create_foreign_key("content_resource", 'mission_content', ['content_uid'], ['uid'])

    with op.batch_alter_table('mission_content', schema=None) as batch_op:
        batch_op.add_column(sa.Column('filename', sa.String(length=255), nullable=True))
        batch_op.drop_column('name')

    with op.batch_alter_table('mission_invitations', schema=None) as batch_op:
        batch_op.add_column(sa.Column('callsign', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('username', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('group_name', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('team_name', sa.String(length=255), nullable=True))
        batch_op.alter_column('client_uid',
               existing_type=sa.String(length=255),
               nullable=True)
        batch_op.create_foreign_key('user', 'user', ['username'], ['username'])
        # batch_op.create_foreign_key('groups', 'groups', ['group_name'], ['group_name'])
        batch_op.create_foreign_key('eud_callsign', 'euds', ['callsign'], ['callsign'])
        batch_op.create_foreign_key('teams', 'teams', ['team_name'], ['name'])
        batch_op.create_foreign_key('eud_uid', 'euds', ['client_uid'], ['uid'])

    with op.batch_alter_table('missions', schema=None) as batch_op:
        batch_op.add_column(sa.Column('group', sa.String(length=255), nullable=True))
        # batch_op.create_foreign_key('groups', 'groups', ['group'], ['group_name'])
        batch_op.drop_column('group_name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('missions', schema=None) as batch_op:
        batch_op.add_column(sa.Column('group_name', sa.String(length=255), nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('group')

    with op.batch_alter_table('mission_invitations', schema=None) as batch_op:
        batch_op.drop_constraint('user', type_='foreignkey')
        batch_op.drop_constraint('eud_callsign', type_='foreignkey')
        batch_op.drop_constraint('eud_uid', type_='foreignkey')
        batch_op.drop_constraint('teams', type_='foreignkey')
        batch_op.alter_column('client_uid',
               existing_type=sa.String(length=255),
               nullable=False)
        batch_op.drop_column('team_name')
        batch_op.drop_column('group_name')
        batch_op.drop_column('username')
        batch_op.drop_column('callsign')

    with op.batch_alter_table('mission_content', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=255), nullable=True))
        batch_op.drop_column('filename')

    with op.batch_alter_table('mission_changes', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('content_uid')

    # ### end Alembic commands ###

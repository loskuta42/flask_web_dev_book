"""add_confirm_field_in_users_table

Revision ID: 4e1085c45ba7
Revises: eec087c3ace3
Create Date: 2022-12-15 17:22:53.268701

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e1085c45ba7'
down_revision = 'eec087c3ace3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('permissions', sa.Integer(), nullable=True))
    op.add_column('roles', sa.Column('default', sa.Boolean(), nullable=True))
    op.create_index(op.f('ix_roles_default'), 'roles', ['default'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_roles_default'), table_name='roles')
    op.drop_column('roles', 'default')
    op.drop_column('roles', 'permissions')
    # ### end Alembic commands ###

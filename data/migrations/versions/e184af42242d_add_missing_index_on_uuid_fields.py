"""Add missing index on UUID fields

Revision ID: e184af42242d
Revises: 6ec8726c0ace
Create Date: 2019-02-14 16:35:47.768086

"""

# revision identifiers, used by Alembic.
revision = "e184af42242d"
down_revision = "6ec8726c0ace"

from alembic import op as original_op
from data.migrations.progress import ProgressWrapper


def upgrade(tables, tester, progress_reporter):
    op = ProgressWrapper(original_op, progress_reporter)
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index("permissionprototype_uuid", "permissionprototype", ["uuid"], unique=False)
    op.create_index("repositorybuildtrigger_uuid", "repositorybuildtrigger", ["uuid"], unique=False)
    op.create_index("user_uuid", "user", ["uuid"], unique=False)
    # ### end Alembic commands ###


def downgrade(tables, tester, progress_reporter):
    op = ProgressWrapper(original_op, progress_reporter)
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index("user_uuid", table_name="user")
    op.drop_index("repositorybuildtrigger_uuid", table_name="repositorybuildtrigger")
    op.drop_index("permissionprototype_uuid", table_name="permissionprototype")
    # ### end Alembic commands ###

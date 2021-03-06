"""Remove replication dedup

Revision ID: 1432b666093e
Revises: b694f05c1169
Create Date: 2020-05-29 16:06:19.379976+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1432b666093e'
down_revision = 'b694f05c1169'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    try:
        with op.batch_alter_table('storage_replication', schema=None) as batch_op:
            batch_op.drop_column('repl_dedup')
    except Exception:
        # Might be already done by migrate113
        pass

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('storage_replication', schema=None) as batch_op:
        batch_op.add_column(sa.Column('repl_dedup', sa.BOOLEAN(), nullable=False))

    # ### end Alembic commands ###

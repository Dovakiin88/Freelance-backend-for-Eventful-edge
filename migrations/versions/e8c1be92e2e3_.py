"""empty message

Revision ID: e8c1be92e2e3
Revises: b0248c9038a5
Create Date: 2023-08-23 20:51:36.193394

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'e8c1be92e2e3'
down_revision = 'b0248c9038a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('template', schema=None) as batch_op:
        batch_op.add_column(sa.Column('saved_template', sa.JSON(), nullable=True))
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('template_issue_number',
               existing_type=sa.INTEGER(),
               type_=sa.String(),
               nullable=True)
        batch_op.alter_column('template_volume_number',
               existing_type=sa.INTEGER(),
               type_=sa.String(),
               nullable=True)
        batch_op.alter_column('template_date',
               existing_type=postgresql.TIMESTAMP(),
               type_=sa.String(length=50),
               nullable=True)
        batch_op.alter_column('template_hoa',
               existing_type=sa.VARCHAR(length=200),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('template', schema=None) as batch_op:
        batch_op.alter_column('template_hoa',
               existing_type=sa.VARCHAR(length=200),
               nullable=False)
        batch_op.alter_column('template_date',
               existing_type=sa.String(length=50),
               type_=postgresql.TIMESTAMP(),
               nullable=False)
        batch_op.alter_column('template_volume_number',
               existing_type=sa.String(),
               type_=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('template_issue_number',
               existing_type=sa.String(),
               type_=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.drop_column('saved_template')

    # ### end Alembic commands ###
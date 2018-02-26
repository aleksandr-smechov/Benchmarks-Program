"""empty message

Revision ID: e42d72d3c94f
Revises: caaf50970a71
Create Date: 2018-02-20 14:07:02.986661

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e42d72d3c94f'
down_revision = 'caaf50970a71'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('list_stats', schema=None) as batch_op:
        batch_op.add_column(sa.Column('cleaned_pct', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('cur_yr_sub_open_rt', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('cur_yr_sub_pct', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('pending_pct', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('subscribed_pct', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('unsubscribed_pct', sa.Float(), nullable=True))
        batch_op.drop_column('unsubscribe_pct')
        batch_op.drop_column('cur_yr_member_pct')
        batch_op.drop_column('clean_pct')
        batch_op.drop_column('cur_yr_members_open_rt')
        batch_op.drop_column('member_pct')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('list_stats', schema=None) as batch_op:
        batch_op.add_column(sa.Column('member_pct', sa.FLOAT(), nullable=True))
        batch_op.add_column(sa.Column('cur_yr_members_open_rt', sa.FLOAT(), nullable=True))
        batch_op.add_column(sa.Column('clean_pct', sa.FLOAT(), nullable=True))
        batch_op.add_column(sa.Column('cur_yr_member_pct', sa.FLOAT(), nullable=True))
        batch_op.add_column(sa.Column('unsubscribe_pct', sa.FLOAT(), nullable=True))
        batch_op.drop_column('unsubscribed_pct')
        batch_op.drop_column('subscribed_pct')
        batch_op.drop_column('pending_pct')
        batch_op.drop_column('cur_yr_sub_pct')
        batch_op.drop_column('cur_yr_sub_open_rt')
        batch_op.drop_column('cleaned_pct')

    # ### end Alembic commands ###
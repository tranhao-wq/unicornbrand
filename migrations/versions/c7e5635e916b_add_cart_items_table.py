"""add cart_items table

Revision ID: c7e5635e916b
Revises: 
Create Date: 2025-07-05 18:47:09.322643

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'c7e5635e916b'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'cart_items',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id'), nullable=False),
        sa.Column('product_id', sa.Integer(), sa.ForeignKey('product.id'), nullable=False),
        sa.Column('quantity', sa.Integer(), nullable=False, default=1),
        sa.Column('size', sa.String(length=20)),
        sa.Column('color', sa.String(length=30)),
        sa.Column('created_at', sa.DateTime()),
        sa.Column('updated_at', sa.DateTime()),
    )

def downgrade():
    op.drop_table('cart_items')

"""initial migration

Revision ID: initial
Create Date: 2025-03-27 10:39:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'initial'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # テーブル作成
    op.create_table(
        'items',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('ex_id', sa.String(50), nullable=False, comment="客先キー"),
        sa.Column('in_id', sa.String(50), nullable=False, comment="社内キー"),
        sa.PrimaryKeyConstraint('id'),
    )

    # インデックス作成
    op.create_index('ix_items_id', 'items', ['id'])
    op.create_index('ix_items_ex_id', 'items', ['ex_id'])
    op.create_index('ix_items_in_id', 'items', ['in_id'])

    # 初期データ挿入
    op.bulk_insert(
        sa.table(
            'items',
            sa.column('id', sa.Integer),
            sa.column('ex_id', sa.String(50)),
            sa.column('in_id', sa.String(50))
        ),
        [
            {'id': 1, 'ex_id': 'tb_89924-X1175-00', 'in_id': '7880_Color_580'},
            {'id': 2, 'ex_id': 'tb_7A3S6-X7V01-00', 'in_id': '2_Color_184E'},
            {'id': 3, 'ex_id': 'tb_71731-X1066-A0', 'in_id': '16791_Color_235'},
            {'id': 4, 'ex_id': 'ts_40456ABC', 'in_id': '2_Color_184E'}
        ]
    )


def downgrade() -> None:
    # テーブル削除
    op.drop_index('ix_items_in_id', 'items')
    op.drop_index('ix_items_ex_id', 'items')
    op.drop_index('ix_items_id', 'items')
    op.drop_table('items')

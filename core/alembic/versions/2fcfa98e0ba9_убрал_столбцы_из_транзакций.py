"""убрал столбцы из транзакций

Revision ID: 2fcfa98e0ba9
Revises: d253d372ad12
Create Date: 2025-01-17 00:31:04.328527

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "2fcfa98e0ba9"
down_revision: Union[str, None] = "d253d372ad12"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(
        "transactions_from_user_id_fkey", "transactions", type_="foreignkey"
    )
    op.drop_constraint(
        "transactions_to_user_id_fkey", "transactions", type_="foreignkey"
    )
    op.drop_column("transactions", "from_user_id")
    op.drop_column("transactions", "to_user_id")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "transactions",
        sa.Column(
            "to_user_id", sa.INTEGER(), autoincrement=False, nullable=False
        ),
    )
    op.add_column(
        "transactions",
        sa.Column(
            "from_user_id", sa.INTEGER(), autoincrement=False, nullable=False
        ),
    )
    op.create_foreign_key(
        "transactions_to_user_id_fkey",
        "transactions",
        "users",
        ["to_user_id"],
        ["id"],
    )
    op.create_foreign_key(
        "transactions_from_user_id_fkey",
        "transactions",
        "users",
        ["from_user_id"],
        ["id"],
    )
    # ### end Alembic commands ###

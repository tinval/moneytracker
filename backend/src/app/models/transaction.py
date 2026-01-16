from datetime import date
from typing import TYPE_CHECKING, Optional

from sqlalchemy import Date, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

if TYPE_CHECKING:
    from .account import Account
    from .category import Category
    from .counterparty import Counterparty
    from .receipt import Receipt
    from .transaction_split import TransactionSplit
    from .user import User


class Transaction(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    date: Mapped[date] = mapped_column(Date, index=True)
    account_id: Mapped[int] = mapped_column(Integer, ForeignKey("accounts.id"))
    counterparty_id: Mapped[int | None] = mapped_column(
        Integer, ForeignKey("counterparties.id"), nullable=True
    )
    category_id: Mapped[int | None] = mapped_column(
        Integer, ForeignKey("categories.id"), nullable=True
    )

    amount: Mapped[float] = mapped_column(Float)  # Signed
    currency_code: Mapped[str] = mapped_column(String(3), ForeignKey("currencies.code"))
    description: Mapped[str | None] = mapped_column(String, nullable=True)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)

    account: Mapped["Account"] = relationship(back_populates="transactions")
    counterparty: Mapped[Optional["Counterparty"]] = relationship(
        back_populates="transactions"
    )
    category: Mapped[Optional["Category"]] = relationship()

    user: Mapped["User"] = relationship(back_populates="transactions")

    splits: Mapped[list["TransactionSplit"]] = relationship(
        back_populates="transaction"
    )
    receipt: Mapped[Optional["Receipt"]] = relationship(
        back_populates="transaction", uselist=False
    )

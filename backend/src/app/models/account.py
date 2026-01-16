import enum
from typing import TYPE_CHECKING

from sqlalchemy import JSON, ForeignKey, Integer, String
from sqlalchemy import Enum as SAEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

if TYPE_CHECKING:
    from .institution import Institution
    from .trade import Trade
    from .transaction import Transaction
    from .user import User


class AccountType(str, enum.Enum):
    CHECKING = "Checking"
    SAVINGS = "Savings"
    INVESTMENT = "Investment"
    CREDIT_CARD = "CreditCard"
    CASH = "Cash"


class Account(Base):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    institution_id: Mapped[int] = mapped_column(Integer, ForeignKey("institutions.id"))
    name: Mapped[str] = mapped_column(String)
    currency_code: Mapped[str] = mapped_column(String(3), ForeignKey("currencies.code"))
    type: Mapped[AccountType] = mapped_column(SAEnum(AccountType))
    details: Mapped[dict | None] = mapped_column(JSON, nullable=True)  # IBAN, etc.

    user: Mapped["User"] = relationship(back_populates="accounts")
    institution: Mapped["Institution"] = relationship(back_populates="accounts")
    transactions: Mapped[list["Transaction"]] = relationship(back_populates="account")
    trades: Mapped[list["Trade"]] = relationship(back_populates="account")

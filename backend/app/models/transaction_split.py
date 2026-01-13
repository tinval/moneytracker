from typing import Optional, TYPE_CHECKING
from sqlalchemy import Integer, String, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base

if TYPE_CHECKING:
    from .transaction import Transaction
    from .category import Category


class TransactionSplit(Base):
    __tablename__ = "transaction_splits"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    transaction_id: Mapped[int] = mapped_column(Integer, ForeignKey("transactions.id"))
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey("categories.id"))
    amount: Mapped[float] = mapped_column(Float)
    description: Mapped[Optional[str]] = mapped_column(String, nullable=True)

    transaction: Mapped["Transaction"] = relationship(back_populates="splits")
    category: Mapped["Category"] = relationship()

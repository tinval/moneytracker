from datetime import date
from typing import TYPE_CHECKING, Optional

from sqlalchemy import Date, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

if TYPE_CHECKING:
    from .document import Document
    from .receipt_item import ReceiptItem
    from .transaction import Transaction


class Receipt(Base):
    __tablename__ = "receipts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    document_id: Mapped[int] = mapped_column(Integer, ForeignKey("documents.id"))
    transaction_id: Mapped[int | None] = mapped_column(
        Integer, ForeignKey("transactions.id"), nullable=True
    )
    category_id: Mapped[int | None] = mapped_column(
        Integer, ForeignKey("categories.id"), nullable=True
    )
    merchant_name: Mapped[str | None] = mapped_column(String, nullable=True)
    date: Mapped[date | None] = mapped_column(Date, nullable=True)
    total_amount: Mapped[float | None] = mapped_column(Float, nullable=True)
    tax_amount: Mapped[float | None] = mapped_column(Float, nullable=True)

    document: Mapped["Document"] = relationship(back_populates="receipt")
    transaction: Mapped[Optional["Transaction"]] = relationship(
        back_populates="receipt"
    )
    items: Mapped[list["ReceiptItem"]] = relationship(back_populates="receipt")

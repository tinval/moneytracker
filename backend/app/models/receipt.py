from typing import Optional, List, TYPE_CHECKING
from sqlalchemy import Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date
from app.database import Base

if TYPE_CHECKING:
    from .document import Document
    from .transaction import Transaction
    from .receipt_item import ReceiptItem


class Receipt(Base):
    __tablename__ = "receipts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    document_id: Mapped[int] = mapped_column(Integer, ForeignKey("documents.id"))
    transaction_id: Mapped[Optional[int]] = mapped_column(
        Integer, ForeignKey("transactions.id"), nullable=True
    )
    category_id: Mapped[Optional[int]] = mapped_column(
        Integer, ForeignKey("categories.id"), nullable=True
    )
    merchant_name: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    total_amount: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    tax_amount: Mapped[Optional[float]] = mapped_column(Float, nullable=True)

    document: Mapped["Document"] = relationship(back_populates="receipt")
    transaction: Mapped[Optional["Transaction"]] = relationship(
        back_populates="receipt"
    )
    items: Mapped[List["ReceiptItem"]] = relationship(back_populates="receipt")

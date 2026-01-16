from typing import TYPE_CHECKING, Optional

from sqlalchemy import Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

if TYPE_CHECKING:
    from .product import Product
    from .receipt import Receipt


class ReceiptItem(Base):
    __tablename__ = "receipt_items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    receipt_id: Mapped[int] = mapped_column(Integer, ForeignKey("receipts.id"))
    product_barcode: Mapped[str | None] = mapped_column(
        String, ForeignKey("products.barcode"), nullable=True
    )
    category_id: Mapped[int | None] = mapped_column(
        Integer, ForeignKey("categories.id"), nullable=True
    )
    description: Mapped[str] = mapped_column(String)
    quantity: Mapped[float | None] = mapped_column(Float, nullable=True)
    unit_price: Mapped[float | None] = mapped_column(Float, nullable=True)
    total_price: Mapped[float | None] = mapped_column(Float, nullable=True)

    receipt: Mapped["Receipt"] = relationship(back_populates="items")
    product: Mapped[Optional["Product"]] = relationship()

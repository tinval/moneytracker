from typing import Optional, TYPE_CHECKING
from sqlalchemy import Integer, String, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base

if TYPE_CHECKING:
    from .receipt import Receipt
    from .product import Product


class ReceiptItem(Base):
    __tablename__ = "receipt_items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    receipt_id: Mapped[int] = mapped_column(Integer, ForeignKey("receipts.id"))
    product_barcode: Mapped[Optional[str]] = mapped_column(
        String, ForeignKey("products.barcode"), nullable=True
    )
    category_id: Mapped[Optional[int]] = mapped_column(
        Integer, ForeignKey("categories.id"), nullable=True
    )
    description: Mapped[str] = mapped_column(String)
    quantity: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    unit_price: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    total_price: Mapped[Optional[float]] = mapped_column(Float, nullable=True)

    receipt: Mapped["Receipt"] = relationship(back_populates="items")
    product: Mapped[Optional["Product"]] = relationship()

from typing import Optional
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class Product(Base):
    __tablename__ = "products"

    barcode: Mapped[str] = mapped_column(String, primary_key=True)  # SKU/Barcode
    name: Mapped[str] = mapped_column(String)
    brand: Mapped[Optional[str]] = mapped_column(String, nullable=True)

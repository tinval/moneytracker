import enum
from typing import List, Optional, TYPE_CHECKING
from sqlalchemy import Integer, String, ForeignKey, Enum as SAEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base

if TYPE_CHECKING:
    from .trade import Trade


class AssetClass(str, enum.Enum):
    STOCK = "Stock"
    ETF = "ETF"
    BOND = "Bond"
    FOREX = "Forex"


class Asset(Base):
    __tablename__ = "assets"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    symbol: Mapped[str] = mapped_column(String, index=True)
    isin: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    name: Mapped[str] = mapped_column(String)
    asset_class: Mapped[AssetClass] = mapped_column(SAEnum(AssetClass))
    currency_code: Mapped[str] = mapped_column(String(3), ForeignKey("currencies.code"))
    exchange: Mapped[Optional[str]] = mapped_column(String, nullable=True)

    trades: Mapped[List["Trade"]] = relationship(back_populates="asset")

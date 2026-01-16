import enum
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, Float, ForeignKey, Integer, String
from sqlalchemy import Enum as SAEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

if TYPE_CHECKING:
    from .account import Account
    from .asset import Asset


class TradeType(str, enum.Enum):
    BUY = "Buy"
    SELL = "Sell"


class Trade(Base):
    __tablename__ = "trades"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    account_id: Mapped[int] = mapped_column(Integer, ForeignKey("accounts.id"))
    asset_id: Mapped[int] = mapped_column(Integer, ForeignKey("assets.id"))
    date: Mapped[datetime] = mapped_column(
        DateTime
    )  # Precise execution time often needed
    type: Mapped[TradeType] = mapped_column(SAEnum(TradeType))
    quantity: Mapped[float] = mapped_column(Float)
    price_per_unit: Mapped[float] = mapped_column(Float)
    commission: Mapped[float] = mapped_column(Float, default=0.0)
    currency_code: Mapped[str] = mapped_column(String(3), ForeignKey("currencies.code"))

    account: Mapped["Account"] = relationship(back_populates="trades")
    asset: Mapped["Asset"] = relationship(back_populates="trades")

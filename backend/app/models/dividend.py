from typing import TYPE_CHECKING
from sqlalchemy import Integer, Float, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date
from app.database import Base

if TYPE_CHECKING:
    from .account import Account
    from .asset import Asset


class Dividend(Base):
    __tablename__ = "dividends"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    account_id: Mapped[int] = mapped_column(Integer, ForeignKey("accounts.id"))
    asset_id: Mapped[int] = mapped_column(Integer, ForeignKey("assets.id"))
    date: Mapped[date] = mapped_column(Date)
    amount: Mapped[float] = mapped_column(Float)
    tax_withheld: Mapped[float] = mapped_column(Float, default=0.0)

    account: Mapped["Account"] = relationship()
    asset: Mapped["Asset"] = relationship()

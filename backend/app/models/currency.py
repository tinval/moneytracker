from datetime import date
from sqlalchemy import Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class Currency(Base):
    __tablename__ = "currencies"

    code: Mapped[str] = mapped_column(String(3), primary_key=True)  # ISO 4217
    name: Mapped[str] = mapped_column(String)
    symbol: Mapped[str] = mapped_column(String, nullable=True)


class ExchangeRate(Base):
    __tablename__ = "exchange_rates"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    date: Mapped[date] = mapped_column(Date, index=True)
    from_currency_code: Mapped[str] = mapped_column(
        String(3), ForeignKey("currencies.code")
    )
    to_currency_code: Mapped[str] = mapped_column(
        String(3), ForeignKey("currencies.code")
    )
    rate: Mapped[float] = mapped_column(Float)

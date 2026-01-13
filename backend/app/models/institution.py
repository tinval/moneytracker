import enum
from typing import Optional, List, TYPE_CHECKING
from sqlalchemy import Integer, String, Enum as SAEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base

if TYPE_CHECKING:
    from .account import Account


class InstitutionType(str, enum.Enum):
    BANK = "Bank"
    BROKER = "Broker"
    CRYPTO_EXCHANGE = "CryptoExchange"
    OTHER = "Other"


class Institution(Base):
    __tablename__ = "institutions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, index=True)
    country_code: Mapped[Optional[str]] = mapped_column(String(2), nullable=True)
    type: Mapped[InstitutionType] = mapped_column(SAEnum(InstitutionType))

    accounts: Mapped[List["Account"]] = relationship(back_populates="institution")

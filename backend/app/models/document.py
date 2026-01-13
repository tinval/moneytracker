import enum
from typing import Optional, TYPE_CHECKING
from sqlalchemy import Integer, String, DateTime, Enum as SAEnum
from sqlalchemy.sql import func
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base

if TYPE_CHECKING:
    from .receipt import Receipt
    from .bank_statement import BankStatement


class DocumentType(str, enum.Enum):
    RECEIPT = "Receipt"
    STATEMENT = "Statement"
    TAX_FORM = "TaxForm"


class Document(Base):
    __tablename__ = "documents"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    path: Mapped[str] = mapped_column(String, unique=True)
    hash: Mapped[str] = mapped_column(String, index=True)
    type: Mapped[DocumentType] = mapped_column(SAEnum(DocumentType))
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    receipt: Mapped[Optional["Receipt"]] = relationship(
        back_populates="document", uselist=False
    )
    bank_statement: Mapped[Optional["BankStatement"]] = relationship(
        back_populates="document", uselist=False
    )

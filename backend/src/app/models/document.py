import enum
from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlalchemy import DateTime, Integer, String
from sqlalchemy import Enum as SAEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from app.database import Base

if TYPE_CHECKING:
    from .bank_statement import BankStatement
    from .receipt import Receipt


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

from typing import Optional, TYPE_CHECKING
from sqlalchemy import Integer, Float, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date
from app.database import Base

if TYPE_CHECKING:
    from .document import Document
    from .account import Account


class BankStatement(Base):
    __tablename__ = "bank_statements"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    document_id: Mapped[int] = mapped_column(Integer, ForeignKey("documents.id"))
    account_id: Mapped[int] = mapped_column(Integer, ForeignKey("accounts.id"))
    date: Mapped[date] = mapped_column(Date)  # Or start_date/end_date
    opening_balance: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    closing_balance: Mapped[Optional[float]] = mapped_column(Float, nullable=True)

    document: Mapped["Document"] = relationship(back_populates="bank_statement")
    account: Mapped["Account"] = relationship()

from typing import Optional, List, TYPE_CHECKING
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base

if TYPE_CHECKING:
    from .user import User
    from .transaction import Transaction


class Counterparty(Base):
    __tablename__ = "counterparties"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[Optional[int]] = mapped_column(
        Integer, ForeignKey("users.id"), nullable=True
    )  # None = Global
    parent_id: Mapped[Optional[int]] = mapped_column(
        Integer, ForeignKey("counterparties.id"), nullable=True
    )

    name: Mapped[str] = mapped_column(String, index=True)
    default_category_id: Mapped[Optional[int]] = mapped_column(
        Integer, ForeignKey("categories.id"), nullable=True
    )
    vat_id: Mapped[Optional[str]] = mapped_column(String, nullable=True)

    user: Mapped[Optional["User"]] = relationship(back_populates="counterparties")
    parent: Mapped[Optional["Counterparty"]] = relationship(
        remote_side=[id], back_populates="children"
    )
    children: Mapped[List["Counterparty"]] = relationship(back_populates="parent")
    transactions: Mapped[List["Transaction"]] = relationship(
        back_populates="counterparty"
    )

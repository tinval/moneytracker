from typing import TYPE_CHECKING, Optional

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

if TYPE_CHECKING:
    from .transaction import Transaction
    from .user import User


class Counterparty(Base):
    __tablename__ = "counterparties"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int | None] = mapped_column(
        Integer, ForeignKey("users.id"), nullable=True
    )  # None = Global
    parent_id: Mapped[int | None] = mapped_column(
        Integer, ForeignKey("counterparties.id"), nullable=True
    )

    name: Mapped[str] = mapped_column(String, index=True)
    default_category_id: Mapped[int | None] = mapped_column(
        Integer, ForeignKey("categories.id"), nullable=True
    )
    vat_id: Mapped[str | None] = mapped_column(String, nullable=True)

    user: Mapped[Optional["User"]] = relationship(back_populates="counterparties")
    parent: Mapped[Optional["Counterparty"]] = relationship(
        remote_side=[id], back_populates="children"
    )
    children: Mapped[list["Counterparty"]] = relationship(back_populates="parent")
    transactions: Mapped[list["Transaction"]] = relationship(
        back_populates="counterparty"
    )

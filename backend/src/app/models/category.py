from typing import TYPE_CHECKING, Optional

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

if TYPE_CHECKING:
    from .user import User


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int | None] = mapped_column(
        Integer, ForeignKey("users.id"), nullable=True
    )  # None = System Default
    name: Mapped[str] = mapped_column(String)
    parent_id: Mapped[int | None] = mapped_column(
        Integer, ForeignKey("categories.id"), nullable=True
    )

    user: Mapped[Optional["User"]] = relationship(back_populates="categories")
    parent: Mapped[Optional["Category"]] = relationship(
        remote_side=[id], back_populates="children"
    )
    children: Mapped[list["Category"]] = relationship(back_populates="parent")
